from django.db.models import query
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
from django.db.models import Count

# Create your views here.

class PaymentCrudViewSet(viewsets.ModelViewSet):
    queryset = payment.objects.all()
    serializer_class = PaymentCrudSerializer

    def get_queryset(self):
        return payment.objects.annotate(
            test=Count('debit'),
        )

class PaymentFilterSet(FilterSet):
    id = filters.CharFilter('id')
    student_id = filters.CharFilter('student_id')

    class Meta:
        model = payment
        fields = ('id', 'student_id')

class PaymentFilterView(generics.ListAPIView):
    queryset = payment.objects.all()
    serializer_class = PaymentCrudSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = PaymentFilterSet

class SponsorPaymentCrudViewSet(viewsets.ModelViewSet):
    queryset = sponsor_payment.objects.all()
    serializer_class = SponsorPaymentCrudSerializer

class SponsorPaymentFilterSet(FilterSet):
    id = filters.CharFilter('id')
    sponsor_id = filters.CharFilter('sponsor_id')

    class Meta:
        model = sponsor_payment
        fields = ('id', 'sponsor_id')

class SponsorPaymentFilterView(generics.ListAPIView):
    queryset = sponsor_payment.objects.all()
    serializer_class = SponsorPaymentCrudSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = SponsorPaymentFilterSet


class SponsorViewSet(viewsets.ModelViewSet):
    queryset = sponsor.objects.all()
    serializer_class = SponsorCrudSerializer

class SponsorBalanceViewSet(viewsets.ModelViewSet):
    queryset = sponsor.objects.all()
    serializer_class = SponsorBalanceSerializer