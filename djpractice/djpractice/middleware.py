from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.utils.deprecation import MiddlewareMixin


class Authenticate(MiddlewareMixin):

    def process_request(self, request):

        if request.path == '/logout/':
            logout(request)
            return HttpResponseRedirect('/')

        elif request.path.split('/')[1] in ['admin', 'css', 'static']:
            return None

        elif request.path == '/login/':
            return self.login(request)

        elif request.user.is_anonymous():
            return HttpResponseRedirect(
                '/admin/login/?next=' + request.path)
