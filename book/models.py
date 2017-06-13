from django.db import models
from django.forms import ModelForm
import django.utils.timezone
import datetime
# Create your models here.
class QRcode(models.Model):
    emailid = models.EmailField(blank=False)
    qrcodeContent=models.CharField(max_length=250,blank=True)
    name=models.CharField(max_length=250,blank=False)
    date=models.DateField(blank=False,default=django.utils.timezone.now)
    time=models.TimeField(blank=False,default=django.utils.timezone.now)
    duration=models.IntegerField(blank=False)
    vehicleNumber=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.emailid


class QRCodeForm(ModelForm):
    # abc=models.CharField(max_length=250,blank=False)

    class Meta:
        model=QRcode
        fields = ['name' , 'duration' , 'emailid' , 'date','time' , 'vehicleNumber' ]

