from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.forms import ModelForm
# from .models import QRcode,QRCodeForm,LoginForm,User
from django.http import HttpResponseRedirect
from django.contrib import messages

def LogoutPage(request):

    response = render(request,'registration/logged_out.html')
    #response.set_cookie('userid', '')  # set blank cookie
    request.session['userid']=''
    return response
