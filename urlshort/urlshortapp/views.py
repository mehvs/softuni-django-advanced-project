from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView
from .forms import ShortenerForm
from django.urls import reverse_lazy
from .models import Url

# Create your views here.

from django.http import HttpResponse


class Index(TemplateView):
    template_name = "urlshortapp/shortener.html"


class CreateShortUrl(CreateView):
    model = Url
    template_name = "urlshortapp/shortener.html"
    fields = ['original_url']
    success_url = reverse_lazy('shortener')

    def form_valid(self, form):
        form.instance.short_code = Url.short_code
        return super(CreateShortUrl, self).form_valid(form)
