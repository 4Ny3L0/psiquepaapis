from rest_framework import serializers
from psiquepaWEB.models import User


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'password')


