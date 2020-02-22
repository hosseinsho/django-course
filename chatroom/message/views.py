from django.shortcuts import render

from users.models import Users
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Messages

def chatpage(request,user_id=None):
    return render(request,'chat.html',
    context={
        'users1': Users.objects.all(),
        'users2': User.objects.all(),
        'receiver' : user_id
    }
    
    )


def add_message(request):
    if request.method== 'POST':
        m=Messages(text=request.POST['text'],
        sender = 1,
        receiver=request.POST['receiver']
        )
        m.save()
    return HttpResponse("message send")