
from rest_framework import serializers

from api_v1.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'