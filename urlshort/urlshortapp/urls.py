from django.urls import path
from .views import Index, CreateShortUrl

urlpatterns = [

    path('', CreateShortUrl.as_view(), name='shortener'),

]
