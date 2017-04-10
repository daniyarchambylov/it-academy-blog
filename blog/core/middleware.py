from django.contrib.auth import login, get_user_model
from django.http.response import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin

User = get_user_model()


class UserAuthMiddleware(MiddlewareMixin):
    def process_request(self, request, *args, **kwargs):
        as_user = request.GET.get('as_user')
        if as_user:
            try:
                user = User.objects.get(id=as_user)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            except:
                pass


class CheckHeader(MiddlewareMixin):
    def process_request(self, request):
        t = request.META.get('HTTP_X_BLOG')
        if t != 'aaa':
            return HttpResponseForbidden()


    def process_response(self, request, response):
        print 'azsxdcfgh'
        return response