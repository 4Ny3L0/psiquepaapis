from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from .errors_messages import ErrorsMessages
from .models import User
from .UserRegistrationSerializer import UserSerializaer
from .registration_messages import RegistrationMessages
from .register_custom_validators import RegisterCustomValidators

# Create your views here.
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def login(request):
    user = get_object_or_404(User, user_name=request.data['user_name'])
    serilizer = UserSerializaer(data=user)
    if serilizer.is_valid():
        user = serilizer.validated_data
    return Response({})


@api_view(['POST'])
def register_user(request):
    request_data = request.data
    serializer = UserSerializaer(data=request.data)
    if serializer.is_valid():
        document_id = request.data['document_id']
        user_name = request.data['user_name']
        if UserSerializaer.user_exists(user_name, document_id):
            return JsonResponse(ErrorsMessages.register_failed, status=status.HTTP_409_CONFLICT)
        serializer.save()
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
