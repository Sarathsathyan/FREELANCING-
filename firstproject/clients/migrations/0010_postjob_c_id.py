# Generated by Django 2.2.1 on 2019-08-21 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0009_client_about_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='postjob',
            name='c_id',
            field=models.IntegerField(null=True),
        ),
    ]