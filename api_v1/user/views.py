

from django.contrib.auth.models import Permission
from rest_framework import generics

from api_v1.user.serializers import PermissionSerializer


class PermissionListCreate(generics.ListCreateAPIView):
    queryset=Permission.objects.all()
    serializer_class=PermissionSerializer

class PermissionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Permission.objects.all()
    serializer_class=PermissionSerializer