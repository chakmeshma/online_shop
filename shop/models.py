from django.db import models


# Create your models here.
class ItemRequest(models.Model):
    link = models.CharField(max_length=1024)
    price = models.FloatField()
    weight = models.IntegerField()
    count = models.IntegerField()
    description = models.TextField()
