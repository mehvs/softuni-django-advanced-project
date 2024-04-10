from django import forms
from .models import Url, User, AbstractUser, Report
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class ShortenerForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ["original_url"]


class LoginForm(AuthenticationForm):
    pass


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = "__all__"
