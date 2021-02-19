from django.db import models

# Create your models here.
class  Groceries(models.Model):
    title=models.CharField(max_length=500)
    description = models.TextField()
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    price = models.FloatField()