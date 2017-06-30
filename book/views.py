# from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render,redirect
from django.forms import ModelForm
from .models import QRcode,QRCodeForm
from oAuth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from decorators import *
import qrcode
from qrcode.image.pure import PymagingImage
from django.http import HttpResponse


@login_required(login_url='/login')
@permission_required(category='AD')
def QRCodesView(request):  #retreive qrcodes, render template and display
    # args={}
    data=QRcode.objects.all()
    return render(request, 'book/list.html', {'qrs' : data})


@login_required(login_url='/login')
@permission_required(category='CL')
def QRCodeCreate(request):
    if request.method=='POST':
        form=QRCodeForm(request.POST)
        if form.is_valid():
            #add record to database
            new_entry=form.save(commit=False)
            new_entry.qrcodeContent = new_entry.name
            new_entry.username=User.objects.get(username=request.COOKIES.get('userid'))
            #to do something with new entry's fields and output a hash
            new_entry.save()
            #response = HttpResponse(content_type="image/png")
            request.session['qrcode_content']=new_entry.qrcodeContent
            #img.save(response,"PNG")
            return render(request,'book/qrcode.html')
            #return HttpResponseRedirect('thanks')

    else:
        form=QRCodeForm()

    return render(request,'book/registration_form.html',{'form':form})

def QRCodeImage(request):
    img = qrcode.make(request.session['qrcode_content'])
    response = HttpResponse(content_type="image/png")
    img.save(response,"PNG")
    return response

def success(request):
    return render(request,'book/thanks.html')




