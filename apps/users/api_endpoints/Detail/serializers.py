from rest_framework.serializers import ModelSerializer
from apps.users.models import User


class UserDetailSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'username',
            'phone',
            'email',
            'photo',
            'date_of_birth',
            'is_active',
            'is_staff',
        )
