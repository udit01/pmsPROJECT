from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.forms import ModelForm
# from .models import QRcode,QRCodeForm,LoginForm,User
from django.http import HttpResponseRedirect
from django.contrib import messages


def LogoutPage(request):
    #set empty cookie
    return render(request,'registration/logged_out.html')
