# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django import forms
import django.utils.timezone
import datetime

#Currently we have a simple username-password model for the user
#Once we have registered as IITD oAuth client we will add other fields
#Also, Loginform will be removed as the user will be redirected to IITD Login page

class User(models.Model):
    password=models.CharField(max_length=100,blank=False)
    username=models.CharField(max_length=100,blank=False)
    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    type = models.CharField(max_length=15)  #Two types- client(can book and edit qrcodes) and admin(for viewing stats and everything)
    def __str__(self):
        return self.type

class LoginForm(forms.ModelForm):

    class Meta:
        model=User
        fields=['username','password']
