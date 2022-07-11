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

class GradesCrudViewSet(viewsets.ModelViewSet):
    queryset = grades.objects.all()
    serializer_class = GradesCrudSerializer

class GradesFilterSet(FilterSet):
    id = filters.CharFilter('id')
    student_id = filters.CharFilter('student_id')
    year = filters.CharFilter('year')
    trimester = filters.CharFilter('trimester')

    class Meta:
        model = grades
        fields = ('id', 'student_id', 'year', 'trimester')

class GradesFilterView(generics.ListAPIView):
    queryset = grades.objects.all()
    serializer_class = GradesCrudSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = GradesFilterSet

class EvaluationFilterView(generics.ListAPIView):
    queryset = grades.objects.all()
    serializer_class = GradesCrudSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = GradesFilterSet