# Generated by Django 2.2.1 on 2019-07-06 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_postjob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='description',
        ),
    ]