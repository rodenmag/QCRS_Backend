from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet
from django_filters import rest_framework as filters
from rest_framework import generics

# Create your views here.
class EnrollmentCrudViewSet(viewsets.ModelViewSet):
    queryset = enrollment.objects.all()
    serializer_class = EnrollmentCrudSerializer

class EnrollmentFilterSet(FilterSet):
    id = filters.CharFilter('id')
    student_id = filters.CharFilter('student_id')
    year_level = filters.CharFilter('year_level')
    trimester = filters.CharFilter('trimester')
    system_id = filters.CharFilter('system_id')

    class Meta:
        model = enrollment
        fields = ('id', 'student_id', 'year_level', 'trimester', 'system_id')

class EnrollmentFilterView(generics.ListAPIView):
    queryset = enrollment.objects.all()
    serializer_class = EnrollmentCrudSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = EnrollmentFilterSet