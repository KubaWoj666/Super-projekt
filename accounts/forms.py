from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username", "password1", "password2",)

class UserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username",)

        

