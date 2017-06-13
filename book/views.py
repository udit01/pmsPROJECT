# from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render,redirect
from django.forms import ModelForm
from .models import QRcode,QRCodeForm
from django.http import HttpResponseRedirect

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
            #to do something with new entry's filds and output a hash
            new_entry.save()

            return HttpResponseRedirect('book/thanks')

    else:
        form=QRCodeForm()

    return render(request,'book/registration_form.html',{'form':form})


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


