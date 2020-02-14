from django.contrib import admin
from .models import Users,Messages

# Register your models here.

@admin.register(Users)
class adminUsers(admin.ModelAdmin):
    pass

@admin.register(Messages)

class adminMessages(admin.ModelAdmin):
    pass