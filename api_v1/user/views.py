
from rest_framework import generics

from api_v1.user.models import User
from api_v1.user.serializers import UserSerializer


class  UserListCreate(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer