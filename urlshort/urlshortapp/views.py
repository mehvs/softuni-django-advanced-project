import requests

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Url, ClickStats
from .forms import ShortenerForm, LoginForm, RegisterForm

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

from django.http import HttpResponse


def redirect_to_original(request, short_code):
    url = Url.objects.get(short_code=short_code)
    url.click_count += 1

    user_agent = request.META.get('HTTP_USER_AGENT', '')

    user_ip = request.META.get('REMOTE_ADDR')

    response = requests.get(f'https://ipinfo.io/{user_ip}/country')

    country_code = ''
    if '400' in response.text.strip():
        country_code = 'n/a'
    else:
        country_code = response.text.strip()

    print(country_code)

    click_stats = ClickStats.objects.create(url_id=url.id, user_agent=user_agent, country_code=country_code)

    click_stats.save()
    url.save()
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


class RegisterView(FormView):
    template_name = 'urlshortapp/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('shortener')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('shortener')
        return super(RegisterView, self).get(*args, **kwargs)


class UrlListView(ListView):
    model = Url
    context_object_name = 'urls'


class UrlDetailView(DetailView):
    model = Url
    context_object_name = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        url = self.get_object()
        click_stats = url.clickstats_set.all()  # Assuming the related_name is 'childmodel_set'
        context['click_stats'] = click_stats
        return context


class UrlUpdateView(UpdateView):
    model = Url
    form_class = ShortenerForm
    success_url = reverse_lazy('urls')


class UrlDeleteView(DeleteView):
    model = Url
    context_object_name = 'url'
    success_url = reverse_lazy('urls')
