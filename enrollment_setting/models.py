from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class enrollment_setting(models.Model):
  miscellaneous = models.FloatField()
  tuition_fee = models.FloatField()
  nstp = models.FloatField()
  year = models.IntegerField()
  trimester = models.IntegerField()
  date_created = models.DateTimeField(auto_now=True)
  posted_by = models.ForeignKey(User, on_delete=models.CASCADE)