# Generated by Django 5.1.7 on 2025-03-13 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_test_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
