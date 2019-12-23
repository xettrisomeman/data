from django import forms 
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm
)

from .models import CustomUser,Post


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomUserAddForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomUserLoginForm(AuthenticationForm):

    class Meta:
        model = CustomUser
        fields = "__all__"

class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
