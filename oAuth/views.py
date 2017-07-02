# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.forms import ModelForm
from .models import LoginForm,User
from django.http import HttpResponseRedirect
from django.contrib import messages

# Currently, a simple login page is rendered which will ask user for username and password
# if login is successful, set cookie and redirect to 'book/'

def LoginPage(request):

    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            new_login=form.save(commit=False)
            #hash the password before checking with the database
            if User.objects.filter(username=new_login.username,password=new_login.password).exists():
                redirect_url = request.session.get('goto', '/book/') #which url to goto after login
                try:
                    del request.session['goto']
                except KeyError:
                    pass
                response=redirect(redirect_url)
                request.session['userid']=new_login.username        #set userid cookie
                return response
            else:
                messages.error(request,"Username or password does not match")    #send error message
    else:
        form=LoginForm()

    return render(request,'book/login.html',{'form':form})