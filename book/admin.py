from django.contrib import admin
from .models  import QRcode
from oAuth.models import UserProfile,User
# Register your models here.

admin.site.register(QRcode)
admin.site.register(User)
admin.site.register(UserProfile)

