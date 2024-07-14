
from django.contrib.auth.models import  Permission, Group
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from api_v1.user.models import User


class UserSerializer(serializers.ModelSerializer):
    errors_messages={
        'required':'El campo es requerido',
        'min_length':'El campo es demasiado corto',
        'max_length':'El campo es demasiado largo',
        'blank':'El campo no puede estar vacio'
    }
    first_name=serializers.CharField(
        required=True,
        min_length=2,
        max_length=50,
        allow_blank=False,
        error_messages=errors_messages
    )
    last_name=serializers.CharField(
        required=True,
        min_length=2,
        max_length=50,
        allow_blank=False,
        error_messages=errors_messages
    )
    password = serializers.CharField(
        write_only=True,
        required=False,  # La contraseña no es obligatoria por defecto
        min_length=8,
        max_length=128,
        error_messages={
            'min_length': 'La contraseña debe tener al menos 8 caracteres.',
            'max_length': 'La contraseña no debe exceder los 128 caracteres.'
        }
    )

    class Meta:
        model=User
        fields='__all__'

    def validate(self,attrs):
        errors={}
        request_method=self.context['request'].method
        if request_method == 'POST' and  not attrs.get('password') :
            errors['password'] = "La contraseña es requerida"
        
        if errors:
            raise serializers.ValidationError(errors)
        return attrs
    
    def create(self,validated_data):
        password= validated_data.pop('password',None)
        user= User(**validated_data)
        user.set_password(password)
        user.save()
        return user
        
    def update(self, instance, validated_data):
        
        for attr, value in validated_data.items():
            if attr == 'password':
                validate_password(value)
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        
        instance.save()
        return instance
    

class PermissionSerializer(serializers.ModelSerializer):
    codename= serializers.CharField(
        required=True,
        min_length=2,
        max_length=50,
        allow_blank=False,
        validators=[
            UniqueValidator(queryset=Permission.objects.all(),message="El codename ya existe")
        ],
        error_messages={
            'required':'El campo es requerido',
            'min_length':'EL campo es demasiado corto',
            'max_length':'El campo es demasiado largo',
            'allow_blank':'el campo no puede estar vacio'
        } 
    )
    name= serializers.CharField(
        required=True,
        min_length=10,
        max_length=50,
        allow_blank=False,
        validators=[
            UniqueValidator(queryset=Permission.objects.all(),message="El codename ya existe")
        ],
        error_messages={
            'required':'El campo es requerido',
            'min_length':'EL campo es demasiado corto',
            'max_length':'El campo es demasiado largo',
            'allow_blank':'el campo no puede estar vacio'
        } 
    )
    class Meta:
        model=Permission
        fields='__all__' 
               
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model= Group
        fields='__all__'            
