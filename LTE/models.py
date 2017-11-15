from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class bands(models.Model):
    country = models.CharField(max_length=50)
    operator = models.CharField(max_length=50)
    bands = models.IntegerField()