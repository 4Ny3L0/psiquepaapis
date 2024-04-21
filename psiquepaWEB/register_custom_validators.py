from rest_framework import serializers
import re
from psiquepaWEB.errors_messages import ErrorsMessages


class RegisterCustomValidators:

    def name_validations(name):
        pass

    def password_validations(password: str):
        pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&._])[A-Za-z\d@$!%*?&._]{8,}$')
        match = pattern.match(password)
        if len(password) < 8:
            raise serializers.ValidationError(ErrorsMessages.min_length)
        if len(password) > 16:
            raise serializers.ValidationError(ErrorsMessages.max_length)
        if not match:
            print(match)
            raise serializers.ValidationError(ErrorsMessages.password_bad_format)

    def user_name_validations(user_name: str):
        if len(user_name) < 8:
            raise serializers.ValidationError(ErrorsMessages.user_name_min)

        if len(user_name) > 25:
            raise serializers.ValidationError(ErrorsMessages.user_name_max)

    def document_id_validations(document_id):
        pattern = re.compile(r'^(1[0-3]|[1-9])-([1-9]\d{0,3})-([1-9]\d{0,3})$')
        match = pattern.match(document_id)
        if not match:
            raise serializers.ValidationError(ErrorsMessages.document_id_format)

    def mobile_number_validations(mobile_number):
        pattern = re.compile(r'^\+5076\d{7}$')
        match = pattern.match(mobile_number)
        if not match:
            raise serializers.ValidationError(ErrorsMessages.mobile_number_format)

    def email_validations(email):
        pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        match = pattern.match(email)
        if not match:
            raise serializers.ValidationError(ErrorsMessages.email_format)
        pass

    def validate_required_entries(values: dict, serializer_class):
        fields = serializer_class.Meta.fields
        for field in fields:
            exist = values.get(field)
            if exist is None:
                raise serializers.ValidationError(ErrorsMessages.field_required)
            if len(str(exist)) == 0:
                raise serializers.ValidationError(ErrorsMessages.field_is_blank)
