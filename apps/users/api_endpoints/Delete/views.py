from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAdminUser
from apps.users.models import User


class DeleteUser(DestroyAPIView):
    """
    Delete user. Authentication is required!
    Only admin user can delete any user
    """
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
    http_method_names = ["delete"]


__all__ = ["DeleteUser"]
