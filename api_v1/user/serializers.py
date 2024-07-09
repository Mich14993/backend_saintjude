# from django.contrib.auth.models import Permission
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers


class PermissionSerializer(serializers.ModelSerializer):
    content_type_id = serializers.PrimaryKeyRelatedField(
        queryset=ContentType.objects.all(),
        error_messages={'required':'El campo tipo de contenido es requerido'}
    )

    class Meta:
        model = Permission
        fields = ["id", "name", "codename", "content_type_id"]
