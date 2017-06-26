from oAuth.models import User
from django.http import HttpResponseRedirect

#decorators needed in the app
def login_required(login_url=None):
    def actual_decorator(func):
        def wrapper(*args,**kwargs):
            request=args[0]
            username=request.COOKIES.get('userid')
            logged_in=False
            if User.objects.filter(username=username).exists():
                logged_in=True
            if(logged_in):
                return func(*args,**kwargs)
            else:
                return HttpResponseRedirect(login_url)
        return wrapper
    return actual_decorator
