from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email_address = models.CharField(max_length=25,null=True)
    password  = models.CharField(max_length=25)
    avatar = models.CharField(max_length=30,default="avatar")
    active = models.BooleanField(default=True)



class Messages(models.Model):
    text = models.TextField()
    sender = models.IntegerField()
    receiver = models.IntegerField()
    date  = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1) #1:send 2:recieve 3:seen