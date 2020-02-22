from django.db import models
#from users.model improt messages mishod zad o kareto bokoni
# Create your models here.
class Messages(models.Model):
    text = models.TextField()
    sender = models.IntegerField()
    receiver = models.IntegerField()
    date  = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1) #1:send 2:recieve 3:seen

    def __str__(self):
        return '%s,%s,%s'%(self.text,self.sender, self.receiver)