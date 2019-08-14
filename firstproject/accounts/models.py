from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    u_id=models.IntegerField()
    role = models.IntegerField()


