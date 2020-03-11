from django.shortcuts import render,redirect
from django.http import HttpResponse , JsonResponse
from .models import Users
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login


from django.middleware.csrf import CsrfViewMiddleware
from django.views.decorators.csrf import csrf_protect , csrf_exempt



def signup(request):
    if request.method=='POST':
        user1 = User.objects.create_user(username=request.POST['user'], email=request.POST['email'],
        password=request.POST['psw'],first_name=request.POST['first'],last_name=request.POST['last'])
        try:
            user1.save()
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



@csrf_exempt

def login_user(request):

    
    user = authenticate(
        request = request,
        username= request.POST['username'],
        password = request.POST['password'])
    
    if user is not None:
        login(request, user)
        return JsonResponse({

            'message' : 'login successfully'
 
        })
    
    else:

        return JsonResponse({

            'message' : 'username or password is wrong'
 
        })
