# Generated by Django 3.1.6 on 2021-02-19 18:06

import blogapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=blogapp.models.upload_path),
            
        ),
    ]