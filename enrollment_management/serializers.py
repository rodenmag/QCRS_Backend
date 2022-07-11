__author__ = 'Roden Magat'
from .models import *
from .serializers import *
from rest_framework import serializers

class EnrollmentCrudSerializer(serializers.ModelSerializer):
    posted_by_name = serializers.SerializerMethodField()
    class Meta:
        model = enrollment
        fields = ('id', 'student_id', 'full_name', 'curriculum_id', 'academic_year', 'trimester' , 'year_level'
        , 'type', 'scholarship', 'total_units', 'gross_fee', 'assessed_amount', 'enrollment_fee', 'prelim'
        , 'midterm', 'finals', 'date_created', 'posted_by', 'posted_by_name', 'miscellaneous', 'nstp', 'tuition_fee', 'system_id')

    def get_posted_by_name(self, obj):
        try:
            qs = obj.posted_by.username
            return qs
        except Exception as ex:
            return None