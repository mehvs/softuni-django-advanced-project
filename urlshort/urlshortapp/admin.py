from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

from .models import User, Url, ClickStats, Report, Support


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'date_joined')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)


class UrlAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_code', 'created_at', 'click_count')
    search_fields = ('original_url', 'short_code')
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'click_count')
    list_per_page = 20


class ClickStatsAdmin(admin.ModelAdmin):
    list_display = ('url', 'click_time', 'country_code', 'user_agent')
    list_filter = ('click_time',)
    search_fields = ('url__original_url', 'country_code')
    list_per_page = 20


class ReportAdmin(admin.ModelAdmin):
    list_display = ('date_of_report', 'suspected_link', 'reason', 'status')
    list_filter = ('date_of_report', 'status')
    search_fields = ('suspected_link', 'reason', 'status')
    readonly_fields = ('date_of_report',)
    list_per_page = 20


class SupportAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email', 'status')
    list_filter = ('status',)
    search_fields = ('subject', 'email')
    list_per_page = 20


admin.site.register(User, UserAdmin)
admin.site.register(Url, UrlAdmin)
admin.site.register(ClickStats, ClickStatsAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Support, SupportAdmin)
