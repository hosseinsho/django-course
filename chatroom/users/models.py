from django.db import models
#import uuid to khode jango
# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=25,unique=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email_address = models.CharField(max_length=25,null=True,unique=True)
    password  = models.CharField(max_length=25)
    avatar = models.CharField(max_length=30,default="avatar")
    active = models.BooleanField(default=True)
    token  = models.UUIDField(null=True)

   # TODO:def neshoon dadan esm
    # def __str__(self):
    #     return '%s,%s'%(self.first_name, self.last_name)
    def get_fullname(self):
        return self.first_name + " " + self.last_name


