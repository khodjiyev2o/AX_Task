from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import IsAdminUser
from apps.users.models import User
from apps.users.api_endpoints.Update.serializers import UpdateUserSerializer


class UpdateUserView(UpdateAPIView):
    """
    Update user information. Admin Authentication is required!
    Send the data in  form-data format if you want to change the photo.
    """
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = (IsAdminUser,)
    parser_classes = (MultiPartParser, JSONParser)


__all__ = ["UpdateUserView"]

