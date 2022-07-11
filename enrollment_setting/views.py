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

class EnrollmentSettingCrudViewSet(viewsets.ModelViewSet):
    queryset = enrollment_setting.objects.all()
    serializer_class = EnrollmentSettingCrudSerializer

class EnrollmentSettingFilterSet(FilterSet):
    id = filters.CharFilter('id')
    year = filters.CharFilter('year')
    trimester = filters.CharFilter('trimester')

    class Meta:
        model = enrollment_setting
        fields = ('id', 'year', 'trimester')

class EnrollmentSettingFilterView(generics.ListAPIView):
    queryset = enrollment_setting.objects.all()
    serializer_class = EnrollmentSettingCrudSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = EnrollmentSettingFilterSet