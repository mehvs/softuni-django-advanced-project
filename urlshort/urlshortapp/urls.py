from django.urls import path
from .views import Index, CreateShortUrl, redirect_to_original, CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', CreateShortUrl.as_view(), name='shortener'),
    path('<str:short_code>/', redirect_to_original, name='redirect'),


]
