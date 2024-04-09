from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, CreateView
from django.urls import reverse_lazy
from .models import Url
from .forms import ShortenerForm, LoginForm

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

from django.http import HttpResponse


def redirect_to_original(request, short_code):
    url = Url.objects.get(short_code=short_code)
    return redirect(url.original_url)


class Index(TemplateView):
    template_name = "urlshortapp/shortener.html"


class CreateShortUrl(CreateView):
    model = Url
    template_name = "urlshortapp/shortener.html"
    form_class = ShortenerForm
    success_url = reverse_lazy('shortener')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.short_code = Url.short_code
        return super(CreateShortUrl, self).form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'urlshortapp/login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('shortener')
