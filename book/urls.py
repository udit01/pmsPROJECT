from django.conf.urls import url
from . import views

app_name='book'

urlpatterns = [
    url(r'^$', views.QRCodeCreate,name='add'),
    url(r'^list/$',views.QRCodesView,name='list'),
    url(r'^thanks/$',views.success),

]