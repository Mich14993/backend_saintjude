# from django.contrib.auth.models import Permission
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class PermissionSerializer(serializers.ModelSerializer):
    content_type_id = serializers.PrimaryKeyRelatedField(
        queryset=ContentType.objects.all(),
        error_messages={'required':'El campo tipo de contenido es requerido'}
    )
    name= serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Permission.objects.all(),message="El nombre del permiso debe ser unico")],
        error_messages={'required':'El nombre del permiso ya existe'}
    )

    codename=serializers.CharField(
        required=True,
        max_length=100,
        min_length=20,
        error_message={
            'required':'El campo codename es requerido',
            'max_length':'El codename es demasiado largo',
            'min_length':'El codename es demasiado corto'
        }
    )

    class Meta:
        model = Permission
        fields = ["id", "name", "codename", "content_type_id"]
