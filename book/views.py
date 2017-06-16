# from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render,redirect
from django.forms import ModelForm
from .models import QRcode,QRCodeForm,LoginForm,User
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def QRCodesView(request):  #retreive qrcodes, render template and display
    # args={}
    data=QRcode.objects.all()
    return render(request, 'book/list.html', {'qrs' : data})

def QRCodeCreate(request):
    if request.method=='POST':
        form=QRCodeForm(request.POST)
        if form.is_valid():
            #add record to database
            new_entry=form.save(commit=False)
            new_entry.qrcodeContent = "89"
            #to do something with new entry's fields and output a hash
            new_entry.save()

            return HttpResponseRedirect('thanks')

    else:
        form=QRCodeForm()

    return render(request,'book/registration_form.html',{'form':form})

def LoginPage(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            new_login=form.save(commit=False)
            #hash the password before checking with the database
            if User.objects.filter(username=new_login.username,password=new_login.password).exists():
                #set userid cookie
                response=redirect('/book/')
                response.set_cookie('userid',new_login.username)
                return response
            else:
                messages.error(request,"Username-password do not match")
                #send error message
    else:
        form=LoginForm()

    return render(request,'book/login.html',{'form':form})

def success(request):
    return render(request,'book/thanks.html')

#
# class AlbumCreate(CreateView):
#     model = Album
#     fields = ['artist', 'album_title', 'genre', 'album_logo']
#
# class AlbumUpdate(UpdateView):
#     model = Album
#     fields = ['artist', 'album_title', 'genre', 'album_logo']
#
# class AlbumDelete(DeleteView):
#     model = Album
#     success_url = reverse_lazy('music:index')
#


