from django.db import models
from users.models import Users
from django.contrib.auth.models import User
import datetime

#from users.model improt messages mishod zad o kareto bokoni
# Create your models here0.



class Conversation(models.Model):
    name = models.CharField(max_length=50)
    is_group = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


class ConversationMember(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation,on_delete=models.CASCADE,null = True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.conversation



class Messages(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(User, on_delete = models.CASCADE)
    
    conversation = models.ForeignKey(Conversation,on_delete=models.CASCADE,null = True)
    
    date  = models.DateTimeField(auto_now_add=True,null =True)
    status = models.IntegerField(default=1) #1:send 2:recieve 3:seen

    def __str__(self):
        return '%s,%s'  %(self.text,self.sender)


 #u  = User.objects.get(username  ='king') 