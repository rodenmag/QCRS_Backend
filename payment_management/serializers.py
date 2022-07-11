__author__ = 'Roden Magat'
import math
from django.db.models import Q
from django.db.models import Sum
from .models import *
from .serializers import *
from rest_framework import serializers
from student_management.models import student


class PaymentCrudSerializer(serializers.ModelSerializer):
    posted_by_name = serializers.SerializerMethodField()
    student_name = serializers.SerializerMethodField()
    test = serializers.SerializerMethodField()
    class Meta:
        model = payment
        fields = ('id', 'student_id', 'description', 'debit', 'credit', 'date', 'date_created', 'posted_by', 'posted_by_name', 'student_name', 'type', 'test')

    def get_posted_by_name(self, obj):
        try:
            qs = obj.posted_by.username
            return qs
        except Exception as ex:
            return None

    def get_student_name(self, obj):
        try:
            qs = obj.student_id.last_name + ', ' + obj.student_id.first_name + ' ' + obj.student_id.middle_name
            return qs
        except Exception as ex:
            return '-'

    def get_test(self, obj):
        return obj.debit


class SponsorPaymentCrudSerializer(serializers.ModelSerializer):
    posted_by_name = serializers.SerializerMethodField()
    sponsor_name = serializers.SerializerMethodField()
    student_name = serializers.SerializerMethodField()
    class Meta:
        model = sponsor_payment
        fields = ('id', 'sponsor_id', 'description', 'debit', 'credit', 'date', 'date_created', 'posted_by', 'posted_by_name', 'sponsor_name', 'student_id', 'student_name')

    def get_posted_by_name(self, obj):
        try:
            qs = obj.posted_by.username
            return qs
        except Exception as ex:
            return None

    def get_sponsor_name(self, obj):
        try:
            qs = obj.sponsor_id.sponsor_name
            return qs
        except Exception as ex:
            return '-'

    def get_student_name(self, obj):
        try:
            qs = obj.student_id.last_name + ', ' + obj.student_id.first_name
            return qs
        except Exception as ex:
            return '-'

class SponsorCrudSerializer(serializers.ModelSerializer):
    posted_by_name = serializers.SerializerMethodField()
    debit = serializers.SerializerMethodField()
    credit = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    value = serializers.SerializerMethodField()
    class Meta:
        model = sponsor
        fields = ('id', 'sponsor_name', 'date_created', 'posted_by', 'posted_by_name', 'debit', 'credit', 'balance', 'label', 'value')

    def get_label(self, obj):
        try:
            qs = obj.sponsor_name
            return qs
        except Exception as ex:
            return None

    def get_value(self, obj):
        try:
            qs = obj.id
            return qs
        except Exception as ex:
            return None

    def get_posted_by_name(self, obj):
        try:
            qs = obj.posted_by.username
            return qs
        except Exception as ex:
            return None

    def get_debit(self, obj):
        try:
            qs = sponsor_payment.objects.filter(sponsor_id=obj.id).aggregate(Sum('debit'))
            return qs['debit__sum']
        except Exception as ex:
            return None

    def get_credit(self, obj):
        try:
            qs = sponsor_payment.objects.filter(sponsor_id=obj.id).aggregate(Sum('credit'))
            return qs['credit__sum']
        except Exception as ex:
            return None

    def get_balance(self, obj):
        try:
            return self.get_debit(obj) - self.get_credit(obj)
        except Exception as ex:
            return None

class SponsorBalanceSerializer(serializers.ModelSerializer):
    debit = serializers.SerializerMethodField()
    credit = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()
    class Meta:
        model = sponsor
        fields = ('sponsor_name', 'debit', 'credit', 'balance')

    def get_debit(self, obj):
        try:
            qs = sponsor_payment.objects.filter(sponsor_id=obj.id).aggregate(Sum('debit'))
            return qs['debit__sum']
        except Exception as ex:
            return None

    def get_credit(self, obj):
        try:
            qs = sponsor_payment.objects.filter(sponsor_id=obj.id).aggregate(Sum('credit'))
            return qs['credit__sum']
        except Exception as ex:
            return None

    def get_balance(self, obj):
        try:
            return self.get_debit(obj) - self.get_credit(obj)
        except Exception as ex:
            return None