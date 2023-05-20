from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from apps.users.api_endpoints.Update.serializers import UpdateUserSerializer


class UpdateUserView(UpdateAPIView):
    """
    Update user information. Authentication is required!
    Send the data in  form-data format if you want to change the photo.
    """

    serializer_class = UpdateUserSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, JSONParser)

    def get_object(self):
        return self.request.user


__all__ = ["UpdateUserView"]
