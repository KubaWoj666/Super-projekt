from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserChangeForm, UserCreationForm
CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = [
        "id",
        "email",
        "username",
        "is_superuser"
    ]

admin.site.register(CustomUser, CustomUserAdmin)