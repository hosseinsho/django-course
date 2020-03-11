from django.shortcuts import render


from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Messages,Conversation
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from django.http import JsonResponse
from django.contrib.auth import authenticate , login

from django.views.decorators.csrf import csrf_protect , csrf_exempt



from rest_framework import serializers






# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()

#vase inke hame field haro befreste ya rahat tar az balayii


class UserSerializer(serializers.ModelSerializer):
#mikhayim az ye method tooye class estefade bokonim 
    name = serializers.SerializerMethodField()
#hala befahme che datayii bayad begire
    def get_name(self,obj):
        return obj.get_full_name()


    class Meta:
        model = User
        exclude = ['password','first_name','last_name']

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
class AddMessageSerilizers(serializers.Serializer):
    #post haro mifresti
    conversation = serializers.IntegerField()
    text  =  serializers.CharField() # mishe inja mahdodiyat haro gozasht mese max length 





def add_message(request):
    print(request.user)

    if not request.user.is_authenticated:
        return JsonResponse({
            'message': 'send login request'


        })
    
    else:
        s= AddMessageSerilizers(data=request.POST)#migii boro data begir hala hamoon data hayiike ba post miyad
        if s.is_valid():
            c= Conversation.objects.get(id= request.POST['conversation'])
            m = Messages(
                text = request.POST['text'],
                sender  = request.user,
                conversation = c
            )
            m.save()
            return JsonResponse ({
                'Messages' : 'your message saved'
            })
        else:
            return JsonResponse ({
                'Messages' : 'send bad request'
            })  





class ConversationSerializer(serializers.ModelSerializer):
    
#age foreign key inaro dari bayad oon chizo over write kard masalan conversation ma fek kon memeber dare ke be user mire mitoonim az class bala estefade bokonim
        #member = UserSerializer(many=True ) many =true yani chand tas toosh for bezan

    class Meta:
        model = Conversation
        fields = '__all__'
#vase conversations list


class MessageSerializer(serializers.ModelSerializer):

    sender = UserSerializer()
    conversation = ConversationSerializer()
    class Meta:
        model = Messages
        fields = '__all__'

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