from django.conf.urls import url
from . import views

app_name='book'

urlpatterns = [
    url(r'^ajax/search$',views.ajax_user_search),
    url(r'^ajax/search/$',views.ajax_user_search),
    url(r'^$', views.QRCodeCreate,name='add'),
    url(r'^list/$',views.QRCodesView,name='list'),
    url(r'^thanks/$',views.success),
    url(r'^qrcode/$',views.QRCodeImage),
]