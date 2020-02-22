from django.contrib import admin

# Register your models here.
from .models import Messages


@admin.register(Messages)

class adminMessages(admin.ModelAdmin):
    pass