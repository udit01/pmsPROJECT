# from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render,redirect
from django.forms import ModelForm
from .models import QRcode,QRCodeForm
from oAuth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from decorators import *

@login_required(login_url='/login')
def QRCodesView(request):  #retreive qrcodes, render template and display
    # args={}
    data=QRcode.objects.all()
    return render(request, 'book/list.html', {'qrs' : data})

@login_required(login_url='/login')
def QRCodeCreate(request):
    if request.method=='POST':
        form=QRCodeForm(request.POST)
        if form.is_valid():
            #add record to database
            new_entry=form.save(commit=False)
            new_entry.qrcodeContent = "xyz"
            new_entry.username=User.objects.get(username=request.COOKIES.get('userid'))
            #to do something with new entry's fields and output a hash
            new_entry.save()

            return HttpResponseRedirect('thanks')

    else:
        form=QRCodeForm()

    return render(request,'book/registration_form.html',{'form':form})


def success(request):
    return render(request,'book/thanks.html')




