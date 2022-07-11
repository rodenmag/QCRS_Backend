from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class subject(models.Model):
  code = models.CharField(max_length=150)
  subject_name = models.CharField(max_length=150)
  unit = models.IntegerField()
  pre_requisite = models.CharField(max_length=150, blank=True, null=True)
  date_created = models.DateTimeField(auto_now=True)
  posted_by = models.ForeignKey(User, on_delete=models.CASCADE)