__author__ = 'Roden Magat'
from .models import *
from .serializers import *
from django.db.models import Sum
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from payment_management.models import payment

class StudentCrudSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    posted_by_name = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    value = serializers.SerializerMethodField()
    debit = serializers.SerializerMethodField()
    credit = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()
    sponsor_name = serializers.SerializerMethodField()
    class Meta:
        model = student
        fields = ('id', 'full_name', 'shs_student_id', 'strand', 'college_student_id', 'course', 'first_name', 'middle_name', 'last_name', 'birthday', 'gender', 'civil_status'
        , 'contact_number', 'parent_contact_number', 'date_created', 'posted_by', 'posted_by_name', 'city_province', 'brgy', 'father_name', 'mother_name', 'elementary_school',
        'junior_high_school', 'senior_high_school', 'college', 'scholarship_percentage', 'label', 'value', 'debit', 'credit', 'balance', 'sponsor_id', 'sponsor_name')

    def get_sponsor_name(self, obj):
        try:
            qs = obj.sponsor_id.sponsor_name
            return qs
        except Exception as ex:
            return None

    def get_posted_by_name(self, obj):
        try:
            qs = obj.posted_by.username
            return qs
        except Exception as ex:
            return None

    def get_full_name(self, obj):
        try:
            qs = obj.first_name + ' ' + obj.last_name
            return qs
        except Exception as ex:
            return None

    def get_label(self, obj):
        try:
            qs = obj.last_name + ', ' + obj.first_name
            return qs
        except Exception as ex:
            return None

    def get_value(self, obj):
        try:
            qs = obj.id
            return qs
        except Exception as ex:
            return None

    def get_debit(self, obj):
        try:
            qs = payment.objects.filter(student_id=obj.id).aggregate(Sum('debit'))
            return qs['debit__sum']
        except Exception as ex:
            return None

    def get_credit(self, obj):
        try:
            qs = payment.objects.filter(student_id=obj.id).aggregate(Sum('credit'))
            return qs['credit__sum']
        except Exception as ex:
            return None

    def get_balance(self, obj):
        try:
            return self.get_debit(obj) - self.get_credit(obj)
        except Exception as ex:
            return None

class StudentBalanceSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    debit = serializers.SerializerMethodField()
    credit = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()
    class Meta:
        model = student
        fields = ('full_name', 'debit', 'credit', 'balance')

    def get_full_name(self, obj):
        try:
            qs = obj.first_name + ' ' + obj.last_name
            return qs
        except Exception as ex:
            return None

    def get_debit(self, obj):
        try:
            qs = payment.objects.filter(student_id=obj.id).aggregate(Sum('debit'))
            return qs['debit__sum']
        except Exception as ex:
            return None

    def get_credit(self, obj):
        try:
            qs = payment.objects.filter(student_id=obj.id).aggregate(Sum('credit'))
            return qs['credit__sum']
        except Exception as ex:
            return None

    def get_balance(self, obj):
        try:
            return self.get_debit(obj) - self.get_credit(obj)
        except Exception as ex:
            return None