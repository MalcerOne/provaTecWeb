# Generated by Django 3.1.7 on 2021-05-17 23:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0016_auto_20210516_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lastmodified',
            name='last_modified',
        ),
        migrations.AddField(
            model_name='lastmodified',
            name='last_modified_data',
            field=models.CharField(default=datetime.date(2021, 5, 17), max_length=20),
        ),
    ]
