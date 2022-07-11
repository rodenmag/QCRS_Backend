__author__ = 'Roden Magat'
from .models import *
from .serializers import *
from rest_framework import serializers
import math
from django.db.models import Q
from django.db.models import Sum

class CurriculumCrudSerializer(serializers.ModelSerializer):
    posted_by_name = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    value = serializers.SerializerMethodField()
    class Meta:
        model = curriculum
        fields = ('id', 'name', 'year', 'remarks', 'date_created', 'posted_by', 'posted_by_name', 'label', 'value')

    def get_posted_by_name(self, obj):
        try:
            qs = obj.posted_by.username
            return qs
        except Exception as ex:
            return None

    def get_label(self, obj):
        try:
            qs = obj.name
            return qs
        except Exception as ex:
            return None

    def get_value(self, obj):
        try:
            qs = obj.id
            return qs
        except Exception as ex:
            return None

class CurriculumContentCrudSerializer(serializers.ModelSerializer):
    posted_by_name = serializers.SerializerMethodField()
    total_units = serializers.SerializerMethodField()
    class Meta:
        model = curriculum_content
        fields = ('id', 'curriculum_id', 'subject_code', 'subject_name', 'unit', 'year', 'trimester', 'date_created', 'posted_by', 'posted_by_name', 'total_units')

    def get_posted_by_name(self, obj):
        try:
            qs = obj.posted_by.username
            return qs
        except Exception as ex:
            return None

    def get_total_units(self, obj):
        request_object = self.context['request']
        #myVariable = request_object.query_params.get('myVariable')
        _year = request_object.query_params.get('year')
        _trimester = request_object.query_params.get('trimester')
        _curriculum_id = request_object.query_params.get('curriculum_id')
        try:
            data = curriculum_content.objects.filter(year=_year, trimester=_trimester, curriculum_id=_curriculum_id)
            data_total = data.values('unit').aggregate(Sum('unit'))
            qs = data_total['unit__sum']
            if qs is None:
                value = 0
            else:
                value = qs
            return value
        except Exception as ex:
            return 0

            

