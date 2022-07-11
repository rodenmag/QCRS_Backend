__author__ = 'Roden Magat'
from .models import *
from .serializers import *
from rest_framework import serializers

class GradesCrudSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    posted_by_name = serializers.SerializerMethodField()
    college_student_id = serializers.SerializerMethodField()
    class Meta:
        model = grades
        fields = ('id', 'student_id', 'college_student_id', 'full_name', 'year', 'trimester', 'subject_code', 'subject_name', 'unit', 'numerical_grade', 'percentage_grade', 'remarks', 'date_created', 'posted_by', 'posted_by_name')

    def get_posted_by_name(self, obj):
        try:
            qs = obj.posted_by.username
            return qs
        except Exception as ex:
            return None

    def get_full_name(self, obj):
        try:
            qs = obj.student_id.last_name + ', ' + obj.student_id.first_name + ' ' + obj.student_id.middle_name
            return qs
        except Exception as ex:
            return None

    def get_college_student_id(self, obj):
        try:
            qs = obj.student_id.college_student_id
            return qs
        except Exception as ex:
            return None

class GradesCrudSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    posted_by_name = serializers.SerializerMethodField()
    class Meta:
        model = grades
        fields = ('full_name', 'year', 'trimester', 'subject_code', 'subject_name', 'unit', 'numerical_grade', 'percentage_grade', 'remarks', 'date_created', 'posted_by_name')

    def get_posted_by_name(self, obj):
        try:
            qs = obj.posted_by.username
            return qs
        except Exception as ex:
            return None

    def get_full_name(self, obj):
        try:
            qs = obj.student_id.last_name + ', ' + obj.student_id.first_name + ' ' + obj.student_id.middle_name
            return qs
        except Exception as ex:
            return None

