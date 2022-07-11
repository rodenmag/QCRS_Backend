from django.db import models
from django.contrib.auth.models import User
from student_management.models import student

# Create your models here.
class grades(models.Model):
  student_id = models.ForeignKey(student, on_delete=models.CASCADE)
  subject_code = models.CharField(max_length=100)
  subject_name = models.CharField(max_length=100)
  unit = models.CharField(max_length=10, null=True, blank=True)
  numerical_grade = models.CharField(max_length=10, null=True, blank=True)
  percentage_grade = models.CharField(max_length=10, null=True, blank=True)
  year = models.CharField(max_length=10, null=True, blank=True)
  trimester = models.CharField(max_length=10, null=True, blank=True)
  remarks = models.CharField(max_length=30)
  date_created = models.DateTimeField(auto_now=True)
  posted_by = models.ForeignKey(User, on_delete=models.CASCADE)