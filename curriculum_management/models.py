from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class curriculum(models.Model):
  name = models.CharField(max_length=150)
  year = models.CharField(max_length=150)
  remarks = models.CharField(max_length=150)
  date_created = models.DateTimeField(auto_now=True)
  posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

class curriculum_content(models.Model):
  curriculum_id = models.ForeignKey(curriculum, on_delete=models.CASCADE)
  subject_code = models.CharField(max_length=150)
  subject_name = models.CharField(max_length=150)
  unit = models.IntegerField()
  year = models.CharField(max_length=150)
  trimester = models.CharField(max_length=150)
  date_created = models.DateTimeField(auto_now=True)
  posted_by = models.ForeignKey(User, on_delete=models.CASCADE)