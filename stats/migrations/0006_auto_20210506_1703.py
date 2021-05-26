# Generated by Django 3.2 on 2021-05-06 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0005_country_flag_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='rank',
            field=models.PositiveSmallIntegerField(unique=True),
        ),
    ]
