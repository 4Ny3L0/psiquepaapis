import jwt
from psiquepa import settings
from psiquepaWEB.login_messges import LoginMessages


class SecurityValidations():
    secret_key = settings.SECRET_KEY
    security_alg = 'HS256'

    def check_session_token(self, token):
        try:
            token_is_valid = jwt.decode(token, self.secret_key, algorithms=self.security_alg)
        except:
            return [LoginMessages.login_invalid_token, False]
        return [token_is_valid, True]

    def generate_session_token(self, user_name):
        payload = dict({'user_name': user_name})
        token_generated = jwt.encode(payload, self.secret_key, algorithm=self.security_alg)
        return token_generated
