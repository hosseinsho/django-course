from django.contrib import admin
from .models import Users

# Register your models here.

@admin.register(Users)
class adminUsers(admin.ModelAdmin):
    list_display = ('first_name','last_name','username')
    list_filter  = ('first_name','last_name','username')

