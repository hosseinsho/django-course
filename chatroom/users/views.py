from django.shortcuts import render

from .models import Users
from django.contrib.auth.models import User

# Create your views here.


def signup(request):
    if request.method=='POST':
        user1 = User.objects.create_user(username=request.POST['user'], email=request.POST['email'],
        password=request.POST['psw'],first_name=request.POST['first'],last_name=request.POST['last'])
        user1.save()
        user2 = Users.objects.create(username=request.POST['user'], email_address=request.POST['email'],
        password=request.POST['psw'],first_name=request.POST['first'],last_name=request.POST['last'])
        user2.save()






    return render(request,'signup.html')