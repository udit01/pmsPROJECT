from django.db import models
from django import forms
import django.utils.timezone
import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    # password=models.CharField(max_length=100,blank=False)
    # username=models.CharField(max_length=100,blank=False)
    def __str__(self):
        return self.username


class QRcode(models.Model):
    emailid = models.EmailField(blank=False)
    qrcodeContent=models.CharField(max_length=250,blank=True)
    name=models.CharField(max_length=250,blank=False)
    date=models.DateField(blank=False,default=django.utils.timezone.now)
    time=models.TimeField(blank=False,default=django.utils.timezone.now)
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

class LoginForm(forms.ModelForm):

    class Meta:
        model=User
        fields=['username','password']
