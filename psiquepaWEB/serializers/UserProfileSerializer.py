from rest_framework import serializers
from psiquepaWEB.models.models import User


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User

    def get_user_profile(self):
        logged_user = 'username12'
        print(logged_user)
        if User.objects.filter(user_name=logged_user):
            user_info = User.objects.get(user_name=logged_user)
            response = dict({'status': 'PS-0000', 'body': dict({
                'first_name': user_info.name,
                'last_name': user_info.last_name,
                'complete_name': f'{user_info.name} {user_info.last_name}',
                'rol': user_info.user_role,
            })})
            return response
        response = dict({'status': 'PS-0000', 'message': 'Not results found'})
        return response
