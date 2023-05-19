from django.contrib import admin
from appUser.models import *



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

   list_display = ('name','user','id')
   


