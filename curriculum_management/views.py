from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet
from django_filters import rest_framework as filters
from rest_framework import generics

# Create your views here.
class CurriculumCrudViewSet(viewsets.ModelViewSet):
    queryset = curriculum.objects.all()
    serializer_class = CurriculumCrudSerializer

class CurriculumFilterSet(FilterSet):
    id = filters.CharFilter('id')

    class Meta:
        model = curriculum
        fields = ('id',)

class CurriculumFilterView(generics.ListAPIView):
    queryset = curriculum.objects.all()
    serializer_class = CurriculumCrudSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = CurriculumFilterSet

class CurriculumContentCrudViewSet(viewsets.ModelViewSet):
    queryset = curriculum_content.objects.all()
    serializer_class = CurriculumContentCrudSerializer


class CurriculumContentFilterSet(FilterSet):
    id = filters.CharFilter('id')
    curriculum_id = filters.CharFilter('curriculum_id')
    year = filters.CharFilter('year')
    trimester = filters.CharFilter('trimester')

    class Meta:
        model = curriculum_content
        fields = ('id', 'curriculum_id', 'year', 'trimester')

class CurriculumContentFilterView(generics.ListAPIView):
    queryset = curriculum_content.objects.all()
    serializer_class = CurriculumContentCrudSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = CurriculumContentFilterSet