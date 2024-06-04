import jwt


class SecurityValidations():
    secret_key = 'Psic0'
    security_alg = 'HS256'

    def check_session_token(self, token):
        token_is_valid = jwt.decode(token, self.secret_key, algorithms=self.security_alg)
        print(token_is_valid)

    def generate_session_token(self, user_name):
        payload = dict({'user_name': user_name})
        secret_key = 'Psic0'
        token_generated = jwt.encode(payload, secret_key, algorithm='HS256')
        return token_generated
