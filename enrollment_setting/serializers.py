__author__ = 'Roden Magat'
from .models import *
from .serializers import *
from rest_framework import serializers

class EnrollmentSettingCrudSerializer(serializers.ModelSerializer):
    posted_by_name = serializers.SerializerMethodField()
    class Meta:
        model = enrollment_setting
        fields = ('id', 'miscellaneous', 'tuition_fee', 'nstp', 'year', 'trimester', 'date_created', 'posted_by', 'posted_by_name')

    def get_posted_by_name(self, obj):
        try:
            qs = obj.posted_by.username
            return qs
        except Exception as ex:
            return None