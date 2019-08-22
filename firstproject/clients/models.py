from django.db import models
from datetime import datetime
# Create your models here.

class Client(models.Model):
    client_id = models.IntegerField(null=True)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=100,null=True)
    department = models.CharField(max_length=100,null=True)
    role = models.CharField(max_length=100,null=True)
    about_company = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class PostJob(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING,null=True)
    Id_client = models.IntegerField(null=True)
    jobtitle = models.CharField(max_length=100)
    jobtype = models.CharField(max_length=100)
    jobcategory = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    tags = models.CharField(max_length=50)
    jobdescription = models.CharField(max_length=100)

    def __str__(self):
        return self.jobtitle






