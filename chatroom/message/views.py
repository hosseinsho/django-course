from django.shortcuts import render

from users.models import Users
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q



def chatpage(request,user_id=None):
#user_id k hamoon reciveer ma ba input hiden k to html bood vaghti mizadim roo linke safhe yaro va adadesh vase ma miyomad
#self_ : miyayim aval ba koki token ok mikoniim migim oon yaro k login shode va tokenesh hamine hala oon yaro idish chiye 
    second = user_id  #hamoon reciver  
    
    if 'token' in request.COOKIES:
        token =  request.COOKIES['token']  #tokeni k az kooki miyad ro begiri
        print(token)

        print(Users.objects.get(id=user_id))
        try:
            u= Users.objects.get(token=token)
            self_ = u.id
            
            
            #messages_s = Messages.objects.filter(sender = self_ , receiver=second)
            #messages_r = Messages.objects.filter(sender = second  , receiver=self_)#inja 2 bar az data base estefade mikonim  ye bar male oonon mij=khayiim ye bar male khodemono
            
            messages = Messages.objects.filter( Q(sender = self_ , receiver=second) | Q(sender = second  , receiver=self_) )

            second_user = Users.objects.get(id=user_id)

        except ObjectDoesNotExist:
                return HttpResponse("TOKEN FALSE",status=401)

        Users_name = {
        u.id : u.get_fullname(),
        second_user.id : second_user.get_fullname()

        }

    return render(request,'chat.html',
    context={
        'users1': Users.objects.all(),
        'users2': User.objects.all(),
        'receiver' : user_id,

        'messages': messages,
        'self_' : self_,
        'Users_name' : Users_name

    }
    
    )


def add_message(request):
    if request.method== 'POST':
        if 'token' in request.COOKIES:
            token=  request.COOKIES['token']
            try:
                u= Users.objects.get(token=token)
                m=Messages(text=request.POST['text'],
                sender = u.id,
                receiver=request.POST['receiver']
                )
                m.save()
                return HttpResponse("message send")
            except ObjectDoesNotExist:
                 return HttpResponse("TOKEN FALSE",status=401)

        else:
            return HttpResponse("login first",status=401)