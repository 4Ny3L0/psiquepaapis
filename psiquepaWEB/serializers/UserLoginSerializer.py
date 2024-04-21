import bcrypt
from rest_framework import serializers, status
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from psiquepaWEB.login_messges import LoginMessages
from psiquepaWEB.models.models import User


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'password')

    def login_user(self):
        user_to_validate = self.validated_data['user_name']
        login_error = ValidationError(LoginMessages.login_invalid)
        login_error.status_code = status.HTTP_401_UNAUTHORIZED
        if User.objects.filter(user_name=user_to_validate).exists():
            access_granted = self.validate_access(self.validated_data['password'])
            if not access_granted:
                raise login_error
            token = 'ksakdkasdlasdlldasldlsadlasdasdas'
            return token
        raise login_error

    def validate_access(self, password):
        user = User.objects.get(user_name=self.validated_data['user_name'])
        checked_password = bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))
        return checked_password
