__author__ = 'Roden Magat'
from .models import *
from .serializers import *
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

class AuthPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('__all__')

class AuthUserGroupsSerializer(serializers.ModelSerializer):
    user_permission = AuthPermissionSerializer(source='permissions', read_only=True, many=True)
    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions', 'user_permission')

class SimpleUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True, max_length=30)
    last_name = serializers.CharField(required=True, max_length=30)
    user_group = AuthUserGroupsSerializer(source='groups', read_only=True, many=True)
    user_permission = AuthPermissionSerializer(source='user_permissions', read_only=True, many=True)
    class Meta:
        model = User
        #fields = ('id', 'username', 'first_name', 'last_name', 'user_group')
        fields = ('id', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'groups', 'user_permissions', 'user_permission', 'user_group')