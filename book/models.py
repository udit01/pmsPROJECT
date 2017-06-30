from __future__ import unicode_literals
from django.db import models
from django import forms
import django.utils.timezone
from oAuth.models import User
import datetime
# Create your models here.



class QRcode(models.Model):
    emailid = models.EmailField(blank=False)
    qrcodeContent=models.CharField(max_length=250,blank=True)
    name=models.CharField(max_length=250,blank=False)
    date=models.DateField(blank=False)
    time=models.TimeField(blank=False)
    duration=models.IntegerField(blank=False)
    vehicleNumber=models.CharField(max_length=100,blank=True)
    username=models.ForeignKey(User,default=2)
    def __str__(self):
        return self.emailid


class QRCodeForm(forms.ModelForm):
    # abc=models.CharField(max_length=250,blank=False)

    class Meta:
        model=QRcode
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'}),
        }
        fields = ['name' , 'duration' , 'emailid' , 'date','time' , 'vehicleNumber' ]


