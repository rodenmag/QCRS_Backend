__author__ = 'Roden Magat'
from .models import *
from .serializers import *
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

class SubjectCrudSerializer(serializers.ModelSerializer):
    posted_by_name = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    value = serializers.SerializerMethodField()
    class Meta:
        model = subject
        fields = ('id', 'code', 'subject_name', 'unit', 'pre_requisite', 'date_created', 'posted_by', 'posted_by_name', 'label', 'value')

    def get_posted_by_name(self, obj):
        try:
            qs = obj.posted_by.username
            return qs
        except Exception as ex:
            return None

    def get_label(self, obj):
        try:
            qs = obj.subject_name + ' - ' + obj.code
            return qs
        except Exception as ex:
            return None

    def get_value(self, obj):
        try:
            qs = obj.id
            return qs
        except Exception as ex:
            return None
