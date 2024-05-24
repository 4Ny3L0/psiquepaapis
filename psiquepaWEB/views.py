from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status

import logging
from .errors_messages import ErrorsMessages
from .UserRegistrationSerializer import UserSerializaer
from .login_messges import LoginMessages
from .registration_messages import RegistrationMessages
from .register_custom_validators import RegisterCustomValidators
from .serializers.UserLoginSerializer import UserLoginSerializer


# Create your views here.
logger = logging.getLogger(__name__)
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        access_token = serializer.login_user()
        return Response(LoginMessages.login_success, status=status.HTTP_200_OK)
    else:
        RegisterCustomValidators.validate_required_entries(values=request.data, serializer_class=serializer)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def register_user(request):
    request_data = request.data
    serializer = UserSerializaer(data=request.data)
    if serializer.is_valid():
        document_id = request.data['document_id']
        user_name = request.data['user_name']
        logger.debug(user_name)
        if serializer.user_exists(user_name, document_id):
            return JsonResponse(ErrorsMessages.register_failed, status=status.HTTP_409_CONFLICT)
        serializer.create_user()
        return JsonResponse(RegistrationMessages.registration_success, status=status.HTTP_201_CREATED)
    else:
        RegisterCustomValidators.validate_required_entries(values=request_data, serializer_class=serializer)
        error = serializer.errors
        error_type = list(serializer.errors.keys())
        return Response(error.get(error_type[0]), status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def blog(request):
    return Response({})


@api_view(['GET'])
def blogs(request):
    return Response({})

@api_view(['GET'])
def user_profile(request):
    return Response(dict({'status': 'PS-0000', 'body': dict({
        'first_name': 'Amberlyn',
        'last_name': 'Gutierrez',
        'rol':1
    })}))
