from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, mixins, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response
from django_filters import FilterSet
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter

# Create your views here.

class SubjectCrudViewSet(viewsets.ModelViewSet):
    queryset = subject.objects.all()
    serializer_class = SubjectCrudSerializer

class SubjectFilterSet(FilterSet):
    id = filters.CharFilter('id')
    code = filters.CharFilter('code')

    class Meta:
        model = subject
        fields = ('id', 'code',)

class SubjectFilterView(generics.ListAPIView):
    queryset = subject.objects.all()
    serializer_class = SubjectCrudSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = SubjectFilterSet