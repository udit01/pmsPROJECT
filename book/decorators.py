from oAuth.models import User,UserProfile
from django.http import HttpResponseRedirect

#decorators needed in the app
def login_required(login_url='/login'):
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
                redirect_url=request.get_full_path()
                request.session['goto'] = redirect_url #storing url to redirect to after login is successful
                response=HttpResponseRedirect(login_url)
                return response
        return wrapper
    return actual_decorator

def permission_required(category='admin',login_url='/login'):
    def actual_decorator(func):
        def wrapper(*args,**kwargs):
            request=args[0]
            username=request.COOKIES.get('userid')
            allowed=False
            user=User.objects.get(username=username)
            if user is not None:
                userCategory=UserProfile.objects.get(user=user).type
                print userCategory
                if(userCategory=='admin' or userCategory==category):
                    allowed=True
            if(allowed):
                return func(*args,**kwargs)
            else:
                redirect_url=request.get_full_path()
                request.session['goto'] = redirect_url #storing url to redirect to after login is successful
                response=HttpResponseRedirect(login_url)
                return response
        return wrapper
    return actual_decorator
