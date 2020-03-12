from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login

from django.http import HttpResponse , JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from message.models import Messages,Conversation

from django.views.decorators.csrf import csrf_protect , csrf_exempt



from rest_framework import serializers,status
from rest_framework.views import APIView
from rest_framework.response import Response

from message.serializers import UserSerializer,AddMessageSerilizers,ConversationSerializer,MessageSerializer,RequestGetMessageSerializer





# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()

#vase inke hame field haro befreste ya rahat tar az balayii


@csrf_exempt
def chatpage(request):
    users = User.objects.all()
   

   #MITOONI BEGI KE  s = UserSerializer(users,many=True) yani be soorate liste
    dict_users = []

    for u in users:
        #object of user midim
        s = UserSerializer(u)
        dict_users.append(s.data)


        # dict_users.append(
        #     {
        #         'first_name': u.first_name,
        #         'last_name' : u.last_name

        #     }
        #)

    r = {
            'users' : dict_users
    }

    print(r)

    return JsonResponse(r)







@csrf_exempt
def message_list(request):

    c = Conversation.objects.get( id = request.GET['conversation'])


    messages = Messages.objects.filter(conversation = c)

    s = MessageSerializer(messages,many=True)

    #  messages_list =  []

    #  for m in messages:
    #      messages_list.append(
    #              {
    #                  'text' : m.text,
    #                  'sender':{
    #                          'first_name': m.sender.first_name,
    #                          'last_name' : m.sender.last_name,
    #                          'id' : m.sender.id
    #                  },
    #                  'date' : m.date,
    #              }


    #      )
    #  d = {

    #      'messages': messages_list

    #  }

    # conversations = []
    # for c in Conversation.objects.all():
    #     t = ConversationSerializer(c).data
    #     conversations.append(t)


    return JsonResponse({'conversations':s.data})






@csrf_exempt
def add_message(request):
    print(request.user)

    if not request.user.is_authenticated:
        return JsonResponse({
            'message': 'send login request'


        })
    
    else:
        s= AddMessageSerilizers(data=request.POST ,        #migii boro data begir hala hamoon data hayiike ba post miyad
        context = {'user':request.user}          #etelate joda dadan be serializer
        )
        if s.is_valid():
            s.save()    #tabe creat ro seda mizane


     
            return JsonResponse ({
                 'Messages' : 'your message saved'
            })
        else:
            print(s.errors) # ye dic az erore ha
            return JsonResponse ({
                'Messages' : 'send bad request',
                'erores' : s.errors
            })  






# baraye inke age post ya get bood karayii bokoni barash if get ... if post...


class message_view(APIView):
    #vasash tabe minevisim tabe get o post


    authentication_classes= [] #... raveshe csrf avaz mikone

    def get(self,request):  #return response vase rest frameworke ke http mide
        z=RequestGetMessageSerializer(data=request.GET)
        if z.is_valid():
            c = Conversation.objects.get( id = request.GET['conversation'])
            messages = Messages.objects.filter(conversation = c)

            s = MessageSerializer(messages,many=True)
            return Response(s.data) 
        else:
            return Response(z.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def post(self,request):
        s= AddMessageSerilizers(data=request.POST ,       
        context = {'user':request.user}         
        )
        if s.is_valid():
            s.save()   

            return Response ({
                 'Messages' : 'your message saved'
            })
        else:
           
            return Response ({
                'Messages' : 'send bad request',
                'erores' : s.errors
            }, status=status.HTTP_400_BAD_REQUEST)#baraye khanayii behtar  
