from django.conf.urls import url
from . import views

app_name='oAuth'


urlpatterns = [
    url(r'^',views.LoginPage),
]