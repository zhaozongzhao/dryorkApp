from django.contrib.auth.models import User,Group
from rest_framework import serializers
#serializers 用于定义api的表现形式，例如返回那些字段，返回怎样的格式

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url','name')
        #fields = '__all__'

from api.models import  Event,Guest

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('url','name','address','start_time','limit','status')

class GuestSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
         model = Guest
         fields= ('url','realnem','phone','email','sign','event')