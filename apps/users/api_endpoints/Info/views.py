
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.users.api_endpoints.Info.serializers import ProfileSerializer


class GetProfileView(RetrieveAPIView):
    """
    Get Profile information. Authentication is required!
    """

    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


__all__ = ["GetProfileView"]