from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

from accounts.models import Profile

admin.site.register(Profile)

