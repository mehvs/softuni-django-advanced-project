from django import forms
from .models import Url, User, AbstractUser
from django.contrib.auth.forms import AuthenticationForm


class ShortenerForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ["original_url"]


class LoginForm(AuthenticationForm):
    pass
