

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v1.user.models import User
from api_v1.user.serializers import UserSerializer
from saintJudeHistory.exceptions.exceptionget import handle_exceptions_get
from saintJudeHistory.exceptions.excgetparams import handle_exceptions_get_params



class UserListCreate(APIView):
    @handle_exceptions_get("Usuarios")
    def get(self,request):
        users=User.objects.all()
        serializer=UserSerializer(users,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=UserSerializer(User,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    
class UserDetailUpdateDestroy(APIView):
    
    @handle_exceptions_get_params("Usuario")
    def get(self,request,pk):
        user=User.objects.get(pk=pk)
        serializer= UserSerializer(user)
        return Response(serializer.data)
    
    
    def put(self,request,pk):
        user=User.objects.get(pk=pk)
        serializer=UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        user=User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    