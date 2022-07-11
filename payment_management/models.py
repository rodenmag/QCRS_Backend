from django.db import models
from django.contrib.auth.models import User
from student_management.models import student

# Create your models here.
class sponsor(models.Model):
  sponsor_name = models.CharField(max_length=100)
  date_created = models.DateTimeField(auto_now=True)
  posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

class payment(models.Model):
  student_id = models.ForeignKey(student, on_delete=models.CASCADE)
  description = models.CharField(max_length=100)
  debit = models.FloatField()
  credit = models.FloatField()
  date = models.DateField()
  type = models.CharField(max_length=100, null=True, blank=True)
  date_created = models.DateTimeField(auto_now=True)
  posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

class sponsor_payment(models.Model):
  sponsor_id = models.ForeignKey(sponsor, on_delete=models.CASCADE)
  student_id = models.ForeignKey(student, on_delete=models.CASCADE, null=True, blank=True)
  description = models.CharField(max_length=100)
  debit = models.FloatField()
  credit = models.FloatField()
  date = models.DateField()
  date_created = models.DateTimeField(auto_now=True)
  posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
