
from rest_framework import serializers

from django.contrib.auth.models import User

from message.models import Messages,Conversation





class UserSerializer(serializers.ModelSerializer):
#mikhayim az ye method tooye class estefade bokonim 
    name = serializers.SerializerMethodField()
#hala befahme che datayii bayad begire
    def get_name(self,obj):
        return obj.get_full_name()


    class Meta:
        model = User
        exclude = ['password','first_name','last_name']





class AddMessageSerilizers(serializers.Serializer):
    #post haro mifresti
    conversation = serializers.IntegerField()
    text  =  serializers.CharField(allow_blank=False) # mishe inja mahdodiyat haro gozasht mese max length 


    #baraye filter gozashtan ro text ba validate_esme onn field
 
    def validate_text(self,data):
        if 'tazahorat' in data:
            raise serializers.ValidationError("bi adab")
        return data
        
    def validate(self,data): #vase hame field ha
        if data['conversation'] != 1 and "enghelab"  in data['text']:
            raise serializers.ValidationError("+18")
        return data



    def create(self , validated_data):           #hamon data ro be onvan paramater mide)
        #validate data hamoon post ro be soorate dict mide ke key oon text o conversaton
        #va obj barmigardoone in tabe
        c= Conversation.objects.get(id= validated_data['conversation'])
        m = Messages(
            text = validated_data['text'],
            sender  = self.context['user'],
            conversation = c
        )
        m.save()
        
        return m 


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

class RequestGetMessageSerializer(serializers.Serializer):
    conversation = serializers.IntegerField()