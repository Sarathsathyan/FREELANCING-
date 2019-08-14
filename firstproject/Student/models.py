from django.db import models
from django.contrib.auth.models import User

class stupro(models.Model):
    stu_id = models.IntegerField()
    nick_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    pincode = models.IntegerField()
    address = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    skills = models.TextField(blank=True)
    project = models.CharField(max_length=100)
    collegename = models.CharField(max_length=100)


    def __str__(self):
        return self.nick_name







# Create your models here.
