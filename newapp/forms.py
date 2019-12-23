from django import forms 
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm
)

from .models import CustomUser


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomUserAddForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

