from rest_framework import serializers
from django.contrib.auth.models import Group,Permission
from ..models import Blog
from django.contrib.auth.hashers import make_password
from .. import roles


class CustomUserReadSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name =  "account serializers"
        model = Blog
        # fields = '__all__' 
        exclude = ['password']
    
   