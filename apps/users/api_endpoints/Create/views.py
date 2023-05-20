
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from apps.users.api_endpoints.Create.serializers import UserCreateSerializer
User = get_user_model()


class CreateUserView(CreateAPIView):
    """
    Create User. Authentication is not required!
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


__all__ = ["CreateUserView"]
