
from django.contrib.auth.models import  Permission,Group
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
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



class AddPermissionToGroup(APIView):
    def post(self,request,group_name):
        
        group= get_object_or_404(Group,name=group_name)
        permission_codenames= request.data.get('permissions',[])
        
        for codename in permission_codenames:
            try:
                perm= Permission.objects.get(codename=codename)
                group.permissions.add(perm)
            except Permission.DoesNotExist:
                return Response({"error":f"Permiso con codename {codename} no existe"},stastus=status.HTTP_400_BAD_REQUEST)
        group.save()
        return Response({"message":"Permisos añadidos correctamente"},status=status.HTTP_200_OK)