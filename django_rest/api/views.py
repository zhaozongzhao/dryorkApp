from django.shortcuts import render

# Create your views here.

from  django.contrib.auth.models import  User,Group
from rest_framework import viewsets
from  api.serializers import UserSerializer,GroupSerializer


#viewsets 定义视图的展现形式

class UserViewSet(viewsets.ModelViewSet):
    '''
    允许用户查看或编辑的api端点
    '''
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViews(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

from  api.serializers import EventSerializer,GuestSerializer
from api.models import Event,Guest

class EventViews(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class GuestViews(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer