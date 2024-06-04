from rest_framework.response import Response

from psiquepaWEB.auth.security_validation import SecurityValidations
from psiquepaWEB.login_messges import LoginMessages
from psiquepaWEB.models.models import User
from rest_framework import authentication, status
from rest_framework import exceptions
import jwt


class AuthCustom(authentication.BaseAuthentication):
    def authenticate(self, request):
        security_validations = SecurityValidations()
        access_token = request.META.get('HTTP_AUTHORIZATION')
        if not access_token:
            return (False, LoginMessages.login_invalid_token)
        response = security_validations.check_session_token(access_token)
        if not response[1]:
            return (False, response[0])
        user_name = response[0]['user_name']
        try:
            user = User.objects.get(user_name=user_name)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('Error')
        return (True, response[0])
