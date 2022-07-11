from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

# Create your views here.
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': SimpleUserSerializer(user, context={'request': request}).data
    }