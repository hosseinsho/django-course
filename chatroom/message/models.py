from django.db import models
from users.models import Users

#from users.model improt messages mishod zad o kareto bokoni
# Create your models here.
class Messages(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(Users, on_delete = models.CASCADE,related_name='senders')
    receiver = models.ForeignKey(Users, on_delete = models.CASCADE,related_name='receivers')
    date  = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1) #1:send 2:recieve 3:seen

    def __str__(self):
        return '%s,%s,%s'%(self.text,self.sender, self.receiver)