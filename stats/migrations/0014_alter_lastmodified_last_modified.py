# Generated by Django 3.2 on 2021-05-15 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0013_lastmodified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastmodified',
            name='last_modified',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
