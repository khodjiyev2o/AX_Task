from rest_framework.serializers import ModelSerializer
from apps.users.models import User


class UserListSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone',
            'email',
            'is_active'
        )
