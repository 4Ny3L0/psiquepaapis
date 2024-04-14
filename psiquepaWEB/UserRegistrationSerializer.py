import bcrypt
from rest_framework import serializers
from .models import User
from .register_custom_validators import RegisterCustomValidators


class UserSerializaer(serializers.ModelSerializer):
    user_name = serializers.CharField(validators=[RegisterCustomValidators.user_name_validations])
    password = serializers.CharField(validators=[RegisterCustomValidators.password_validations])
    name = serializers.CharField(validators=[RegisterCustomValidators.name_validations])

    class Meta:
        model = User
        fields = ['name', 'last_name', 'document_id_type', 'document_id', 'user_name', 'password']

    def user_exists(self, user_to_validate, document_id):
        if User.objects.filter(user_name=user_to_validate).exists() or User.objects.filter(
                document_id=document_id).exists():
            return True
        else:
            return False

    def password_encryption(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def create_user(self):
        plain_pass = self.validated_data.pop('password')
        password_secure = self.password_encryption(plain_pass)
        User.objects.create(password=password_secure, **self.validated_data)