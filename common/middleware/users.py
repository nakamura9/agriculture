from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages


class UserTestMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        '''
        Middleware that evaluates a requests user and determines whether the 
        user should be granted access to the page.
       
        '''

        redirect = request.META.get('HTTP_REFERER', None)
        if request.user.is_superuser or \
                hasattr(request.user, 'profile') or \
                request.path.startswith("/login") or \
                "profile" in request.path or \
                request.path.startswith("/admin") or \
                request.path.startswith("/marketplace") or \
                request.path.startswith("/blog"):
            
            return self.get_response(request)
        
        else:
            messages.info(request, "You must be logged in to access this feature")
            return HttpResponseRedirect(
                "/login/?next={}".format(redirect) if redirect else "/login/")
        