from rest_framework import serializers
from psiquepaWEB.errors_messages import ErrorsMessages


class RegisterCustomValidators:

    def password_validations(password):
        if len(password) < 8:
            raise serializers.ValidationError(ErrorsMessages.min_length)
        if len(password) > 16:
            raise serializers.ValidationError(ErrorsMessages.max_length)
