from django.db import models
from django.contrib.auth.models import User
#from payment_management.models import sponsor

# Create your models here.
class student(models.Model):
  shs_student_id = models.CharField(max_length=20, blank=True, null=True)
  strand = models.CharField(max_length=150, blank=True, null=True)
  college_student_id = models.CharField(max_length=20, blank=True, null=True)
  course = models.CharField(max_length=150, blank=True, null=True)
  first_name = models.CharField(max_length=50)
  middle_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  birthday = models.DateField()
  gender = models.CharField(max_length=50)
  civil_status = models.CharField(max_length=50)
  contact_number = models.CharField(max_length=50)
  parent_contact_number = models.CharField(max_length=50, blank=True, null=True)
  city_province = models.CharField(max_length=150, blank=True, null=True)
  brgy = models.CharField(max_length=150, blank=True, null=True)
  father_name = models.CharField(max_length=50, blank=True, null=True)
  mother_name = models.CharField(max_length=50, blank=True, null=True)
  elementary_school = models.CharField(max_length=100, blank=True, null=True)
  junior_high_school = models.CharField(max_length=100, blank=True, null=True)
  senior_high_school = models.CharField(max_length=100, blank=True, null=True)
  college = models.CharField(max_length=100, blank=True, null=True)
  scholarship_percentage = models.IntegerField(blank=True, null=True)
  date_created = models.DateTimeField(auto_now=True)
  posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
  sponsor_id = models.ForeignKey('payment_management.sponsor', on_delete=models.CASCADE, null=True, blank=True)