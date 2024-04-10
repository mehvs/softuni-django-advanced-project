from django.urls import path
from .views import CreateShortUrl, redirect_to_original, CustomLoginView, RegisterView, UrlListView, \
    UrlDetailView, UrlUpdateView, UrlDeleteView, CreateReportView, ListReportView, ReportUpdateView, ReportDeleteView, \
    CreateSupportView, ListSupportView, SupportUpdateView
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('', CreateShortUrl.as_view(), name='shortener'),
    path('urls', UrlListView.as_view(), name='urls'),
    path('url/<int:pk>/', UrlDetailView.as_view(), name='url'),
    path('url-update/<int:pk>/', UrlUpdateView.as_view(), name='url-update'),
    path('url-delete/<int:pk>/', UrlDeleteView.as_view(), name='url-delete'),

    path('report-create/', CreateReportView.as_view(), name='report-create'),
    path('report-list/', ListReportView.as_view(), name='report-list'),
    path('report-update/<int:pk>/', ReportUpdateView.as_view(), name='report-update'),
    path('report-delete/<int:pk>/', ReportDeleteView.as_view(), name='report-delete'),

    path('support-create/', CreateSupportView.as_view(), name='support-create'),
    path('support-list/', ListSupportView.as_view(), name='support-list'),
    path('support-update/<int:pk>/', SupportUpdateView.as_view(), name='support-update'),

    path('<str:short_code>/', redirect_to_original, name='redirect'),

]
