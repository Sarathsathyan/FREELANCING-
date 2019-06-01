from django.db import models
from clients.models import Client
from datetime import datetime
# Create your models here.

class Listing(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=200)
    duration = models.IntegerField()
    experiance_level = models.CharField(max_length=200)
    paid_unpaid = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    paid_unpaid = models.CharField(max_length=200)
    list_date = models.DateField(default=datetime.now,blank=True)
    def __str__(self):
        return self.title