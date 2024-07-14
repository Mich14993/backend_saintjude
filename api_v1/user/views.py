from django.contrib.auth.models import  Permission,Group
from rest_framework import generics
from api_v1.user.models import User
from api_v1.user.serializers import GroupSerializer, PermissionSerializer, UserSerializer


class UserListCreate(generics.ListCreateAPIView):
    queryset= User.objects.all()
    serializer_class=UserSerializer
    
class UserDetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class PermissionListCreate(generics.ListCreateAPIView):
    queryset=Permission.objects.all()
    serializer_class=PermissionSerializer

class PermissionDetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Permission.objects.all()
    serializer_class=PermissionSerializer

class GroupListCreate(generics.ListCreateAPIView):
    queryset= Group.objects.all()
    serializer_class=GroupSerializer

class GroupDetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Group.objects.all()
    serializer_class=GroupSerializer
