from django.db import models
from django.utils import timezone
from datetime import datetime
from django.conf import settings
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()