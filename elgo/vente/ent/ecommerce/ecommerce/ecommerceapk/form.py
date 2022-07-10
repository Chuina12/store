from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

from .models import UserModel

# User = settings.AUTH_USER_MODEL

class UserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = [
            'username',
            'numero',
            'ville',
            'password1',
            'password2'
        ]