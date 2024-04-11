from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from .errors_messages import ErrorsMessages
from .models import User
from .UserRegistrationSerializer import UserSerializaer
from .registration_messages import RegistrationMessages


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
    success_message = RegistrationMessages.registration_success
    serializer = UserSerializaer(data=request.data)
    document_id = request.data['document_id']
    user_name = request.data['user_name']
    if User.objects.filter(user_name=user_name).exists() or User.objects.filter(document_id=document_id).exists():
        return JsonResponse(ErrorsMessages.register_failed, status=status.HTTP_409_CONFLICT)
    else:
        serializer = UserSerializaer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(success_message, status=status.HTTP_201_CREATED)
        else:
            #error = serializer.password_validations(data=request.data)
            print(serializer.errors)
            return JsonResponse(serializer.errors.get('password'), status=status.HTTP_400_BAD_REQUEST)
    #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def blog(request):
    return Response({})


@api_view(['GET'])
def blogs(request):
    return Response({})
