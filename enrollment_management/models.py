from curriculum_management.models import curriculum
from django.db import models
from django.contrib.auth.models import User
from curriculum_management.models import curriculum
from student_management.models import student

# Create your models here.
class enrollment(models.Model):
  system_id = models.ForeignKey(student, on_delete=models.CASCADE, blank=True, null=True)
  student_id = models.CharField(max_length=150)
  full_name = models.CharField(max_length=150)
  curriculum_id = models.ForeignKey(curriculum, on_delete=models.CASCADE)
  #curriculum_name = models.CharField(max_length=150)
  academic_year = models.CharField(max_length=50)
  trimester = models.CharField(max_length=50)
  year_level = models.CharField(max_length=50)
  type = models.CharField(max_length=150)
  scholarship = models.FloatField()
  total_units = models.FloatField()
  gross_fee = models.FloatField()
  assessed_amount = models.FloatField()
  enrollment_fee = models.FloatField()
  prelim = models.FloatField()
  midterm = models.FloatField()
  finals = models.FloatField()
  miscellaneous = models.FloatField(blank=True, null=True)
  nstp = models.FloatField(blank=True, null=True)
  tuition_fee = models.FloatField(blank=True, null=True)
  date_created = models.DateTimeField(auto_now=True)
  posted_by = models.ForeignKey(User, on_delete=models.CASCADE)