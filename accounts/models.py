from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to="accounts/", blank=True, null=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


    def __str__(self):
        return self.username

   
   