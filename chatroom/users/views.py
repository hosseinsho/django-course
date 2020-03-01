from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Users
from django.contrib.auth.models import User
import uuid
# Create your views here.


def signup(request):
    if request.method=='POST':
        user1 = User.objects.create_user(username=request.POST['user'], email=request.POST['email'],
        password=request.POST['psw'],first_name=request.POST['first'],last_name=request.POST['last'])
        try:
            user1.save()
        except:
            return HttpResponse("we have this username",status=400)

        user2 = Users.objects.create(username=request.POST['user'], email_address=request.POST['email'],
        password=request.POST['psw'],first_name=request.POST['first'],last_name=request.POST['last'])
        try:
            user2.save()
        except:
            return HttpResponse("we have this username",status=400)

        return render(request,'signup.html')

    elif(request.method =='GET'):
        users1=User.objects.all()
        return render(request,
        'signup.html',
        context={
            'users1':users1


        }
        )


def login(request):
    if request.method=='GET':

        return render(request,'login.html',
        context={
            
          #'username_valied': u[0]

        }
        
        
        )
        #ba pass adad moshkel dare bayad bebinam vase user jango cheoori mishe login karad
    elif request.method=='POST':
        u= Users.objects.filter(username=request.POST['username']
        ,password=request.POST['psw'] )


        print("login OK",u)
        if u:
            u[0].token = uuid.uuid4()
            u[0].save()
            print("token saved")
            response= redirect('/message/')
            response.set_cookie('token',u[0].token)
            return response
        else:
            return redirect('/users/login/')



