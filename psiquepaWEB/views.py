from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

import logging

from rest_framework_simplejwt.authentication import JWTAuthentication

from .auth.AuthCustom import AuthCustom
from .errors_messages import ErrorsMessages
from .UserRegistrationSerializer import UserSerializaer
from .login_messges import LoginMessages
from .registration_messages import RegistrationMessages
from .register_custom_validators import RegisterCustomValidators
from .serializers.BlogSerializer import BlogSerializer
from .serializers.UserLoginSerializer import UserLoginSerializer
from .serializers.UserProfileSerializer import UserProfileSerializer

# Create your views here.
logger = logging.getLogger(__name__)


@api_view(['POST'])
def login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        access_token = serializer.login_user()
        new_response = LoginMessages.login_success.copy()
        new_response['token'] = access_token
        return Response(new_response, status=status.HTTP_200_OK)
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
    if request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.create_blog()
            return Response(result)
        if serializer.errors:
            return Response(serializer.errors)
    if request.method == 'PUT':
        return Response({'status': 'MODIFIED'})
    if request.method == 'DELETE':
        serializer = BlogSerializer()
        return Response({'status': 'DELETED'})
    return Response()


@api_view(['GET', 'DELETE'])
def blog_detailed(request, blog_id):
    if request.method == 'GET':
        serializers = BlogSerializer()
        blog_detail = serializers.get_blog_by_id(blog_id=blog_id)
        return Response(blog_detail[0], status=blog_detail[1])
    if request.method == 'DELETE':
        serializers = BlogSerializer()
        process_result = serializers.delete_blog_by_id(blog_id=blog_id)
        return Response(process_result[0], process_result[1])


@api_view(['GET'])
def blogs(request):
    serializers = BlogSerializer().get_all_blogs()
    return Response(serializers[0], status=serializers[1])


@api_view(['GET'])
@authentication_classes([AuthCustom])
@permission_classes([IsAuthenticated])
def user_profile(request):
    serializer = UserProfileSerializer()
    response = serializer.get_user_profile()
    return Response(response[0], status=response[1])
