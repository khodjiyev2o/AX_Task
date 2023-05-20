from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path

from .api_endpoints import List, Detail, Info, Create, Update, Delete

application_urlpatterns = [
    path('', List.UserListView.as_view(), name='users-list'),
    path('<int:pk>/', Detail.UserDetailView.as_view(), name='user-detail-by-id'),
    path('me/', Info.GetProfileView.as_view(), name='user-profile'),
    path('create/', Create.CreateUserView.as_view(), name='user-create'),
    path('update/<int:pk>/', Update.UpdateUserView.as_view(), name='user-update'),
    path('delete/<int:pk>/', Delete.DeleteUser.as_view(), name='user-delete'),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
urlpatterns = application_urlpatterns
