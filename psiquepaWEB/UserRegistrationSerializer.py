from .models import User
from rest_framework import serializers
from .register_custom_validators import RegisterCustomValidators


class UserSerializaer(serializers.ModelSerializer):

    password = serializers.CharField(validators=[RegisterCustomValidators.password_validations])

    class Meta:
        model = User
        fields = '__all__'


