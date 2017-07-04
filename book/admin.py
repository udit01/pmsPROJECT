from django.contrib import admin
from .models  import QRcode
from oAuth.models import UserProfile,User
# Register your models here.

class CustomAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields ]#if field.name != "id"]
        super(CustomAdmin, self).__init__(model, admin_site)



admin.site.register(QRcode,CustomAdmin)
admin.site.register(User,CustomAdmin)
admin.site.register(UserProfile,CustomAdmin)

