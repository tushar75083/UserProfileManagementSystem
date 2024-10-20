from django.contrib import admin
from .models import UserProfile
# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email','password','age','date_of_birth','profile_image','bio']
    list_filter=['first_name']