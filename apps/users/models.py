from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from apps.common.models import BaseModel
from .managers import UserManager
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser, BaseModel):
    first_name = models.CharField(_("First Name"), max_length=255, null=True, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=255, null=True, blank=True)
    middle_name = models.CharField(_("Middle Name"), max_length=255, null=True, blank=True)
    username = models.CharField(_("Username"), max_length=255, unique=True, null=True, blank=True)
    phone = PhoneNumberField(_("Phone number"), max_length=32, unique=True, null=True, blank=True)
    email = models.EmailField(_("Email"), max_length=255, unique=True)
    photo = models.ImageField(_("Photo"), upload_to='users/%Y/%m', blank=True, null=True)
    date_of_birth = models.DateField(_("Data of Birth"), blank=True, null=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # type: ignore

    def __str__(self):
        if self.email:
            return self.email
        if self.phone:
            return f"{self.phone}"
        if self.username:
            return self.username

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def tokens(self):
        token = RefreshToken.for_user(self)
        return {'access': str(token.access_token), 'refresh': str(token)}

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
