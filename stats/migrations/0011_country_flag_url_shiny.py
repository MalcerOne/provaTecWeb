# Generated by Django 3.2 on 2021-05-15 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0010_country_name_pt'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='flag_url_shiny',
            field=models.URLField(null=True),
        ),
    ]
