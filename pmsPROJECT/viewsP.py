from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.forms import ModelForm
# from .models import QRcode,QRCodeForm,LoginForm,User
from django.http import HttpResponseRedirect
from django.contrib import messages


@login_required(login_url = '/login')
def home(request):
    login_url = '/login'
    REDIRECT_FIELD_NAME = '/login'
    # data=QRcode.objects.all()
    return render(request, 'registration/home.html')


def oauthLogin(request):
    pass