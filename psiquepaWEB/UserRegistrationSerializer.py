from .errors_messages import ErrorsMessages
from .models import User
from rest_framework import serializers
from .register_custom_validators import RegisterCustomValidators


class UserSerializaer(serializers.ModelSerializer):
    user_name = serializers.CharField(validators=[RegisterCustomValidators.user_name_validations])
    password = serializers.CharField(validators=[RegisterCustomValidators.password_validations])

    class Meta:
        model = User
        fields = ['name', 'last_name', 'document_id_type', 'document_id', 'user_name', 'password']

    def user_exists(user, document_id):
        if User.objects.filter(user_name=user).exists() or User.objects.filter(document_id=document_id).exists():
            return True
        else:
            return False
