from django.http import HttpResponseRedirect
from django.urls import reverse


class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and not request.user.is_superuser:
            if not request.user.groups.filter(name__in=['superusers', 'staff']).exists():
                return HttpResponseRedirect(reverse('admin_access_denied'))
        return self.get_response(request)
