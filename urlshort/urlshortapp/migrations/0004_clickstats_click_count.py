# Generated by Django 5.0.4 on 2024-04-08 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortapp', '0003_clickstats'),
    ]

    operations = [
        migrations.AddField(
            model_name='clickstats',
            name='click_count',
            field=models.IntegerField(default=0),
        ),
    ]