from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAdminUser

from apps.users.api_endpoints.Detail.serializers import UserDetailSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class UserDetailView(RetrieveAPIView):
    """
    Get user information by id. Authentication is required!
    Only admin can access it !
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (IsAdminUser,)


__all__ = ["UserDetailView"]
