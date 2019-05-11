from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    postname = models.CharField(max_length=100)
    postbody = models.CharField(max_length=10000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateField(default=timezone.now)        
