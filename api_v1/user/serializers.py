
from rest_framework import serializers

from api_v1.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
    
    def create(self,validated_data):
        return User.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.email=validated_data.get('email', instance.email)
        instance.password=validated_data.get('password',instance.password)
        instance.is_superuser=validated_data.get('is_superuser',instance.is_superuser)
        instance.first_name= validated_data.get('first_name',instance.first_name)
        instance.last_name=validated_data.get('last_name',instance.last_name)
        instance.image=validated_data.get('is_staff',instance.is_staff)
        instance.is_active=validated_data.get('is_active',instance.is_active)
        instance.save()
        return instance
    
    