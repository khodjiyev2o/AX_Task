from django.contrib import admin
from django.urls import path, include
from .swagger import swaggerurlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/users/", include("apps.users.urls")),
]

urlpatterns += swaggerurlpatterns
