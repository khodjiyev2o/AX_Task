from rest_framework.generics import ListAPIView
from apps.users.models import User
from apps.users.api_endpoints.List.serializers import UserListSerializer
from rest_framework.permissions import IsAdminUser


class UserListView(ListAPIView):
    """
    Only an admin user can access this endpoint,
    Unsecure to allow any user to see  all users.
    """
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAdminUser]
    search_fields = ['first_name', 'email', 'username']
    filterset_fields = ['is_staff', 'is_active', 'is_superuser']


__all__ = ["UserListView"]
