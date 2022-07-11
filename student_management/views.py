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

class StudentBalanceViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = StudentBalanceSerializer

class StudentCrudViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = StudentCrudSerializer

class StudentFilterSet(FilterSet):
    id = filters.CharFilter('id')

    class Meta:
        model = student
        fields = ('id',)

class StudentFilterView(generics.ListAPIView):
    queryset = student.objects.all()
    serializer_class = StudentCrudSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = StudentFilterSet

"""
class CollegeStudentCrudViewset(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = college.objects.all()
    serializer_class = CollegeStudentCrudSerializer

    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        if not is_many:
            return super(CollegeStudentCrudViewset, self).create(request, *args, **kwargs)
        else:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class SeniorHighStudentCrudViewset(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = senior_high.objects.all()
    serializer_class = SeniorHighStudentCrudSerializer

    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        if not is_many:
            return super(SeniorHighStudentCrudViewset, self).create(request, *args, **kwargs)
        else:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class OtherInfoStudentCrudViewset(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = others.objects.all()
    serializer_class = OtherInfoStudentCrudSerializer

    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        if not is_many:
            return super(OtherInfoStudentCrudViewset, self).create(request, *args, **kwargs)
        else:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
"""
