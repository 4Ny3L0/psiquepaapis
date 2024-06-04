from psiquepaWEB.models.models import User
from rest_framework import authentication
from rest_framework import exceptions
import jwt


class AuthCustom(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('HTTP_AUTHORIZATION')
        print(username)


        if not username:
            return None

        try:
            user = User.objects.get(user_name=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)
