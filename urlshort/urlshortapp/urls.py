from django.urls import path
from .views import Index, CreateShortUrl, redirect_to_original, CustomLoginView, RegisterView, UrlListView, \
    UrlDetailView
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('urls', UrlListView.as_view(), name='urls'),
    path('url/<int:pk>/', UrlDetailView.as_view(), name='url'),

    path('', CreateShortUrl.as_view(), name='shortener'),
    path('<str:short_code>/', redirect_to_original, name='redirect'),

]
