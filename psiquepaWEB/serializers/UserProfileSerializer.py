from rest_framework import serializers, status
from rest_framework.response import Response

from psiquepaWEB.models.models import User


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User

    def get_user_profile(self):
        logged_user = 'username12'
        if User.objects.filter(user_name=logged_user):
            user_info = User.objects.get(user_name=logged_user)
            response = dict({'status': 'PS-0000', 'body': dict({
                'first_name': user_info.name,
                'last_name': user_info.last_name,
                'complete_name': f'{user_info.name} {user_info.last_name}',
                'rol': user_info.user_role,
            })})
            return response
        response = dict({'status': 'PS-0020', 'message': 'No results found'})
        return [response, status.HTTP_404_NOT_FOUND]
