from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import User
from .UserSerializer import UserSerializaer


# Create your views here.
@api_view(['POST'])
def login(request):
    user = User.objects
    return Response({})


@api_view(['POST'])
def register_user(request):
    success_message = {'status': 'PS-0000', 'message': 'User created successfully'}
    serializer = UserSerializaer(data=request.data)
    document_id = request.data['document_id']
    user_name = request.data['user_name']
    print(document_id)
    if User.objects.filter(user_name=user_name).exists() or User.objects.filter(document_id=document_id).exists():
        error = {'status': 'PS-0001', 'message': 'Error during user registration'}
        return JsonResponse(error, status=400)
    else:
        serializer = UserSerializaer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(success_message, status=200)
    return Response(serializer.errors, status=400)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def blog(request):
    return Response({})


@api_view(['GET'])
def blogs(request):
    return Response({})
