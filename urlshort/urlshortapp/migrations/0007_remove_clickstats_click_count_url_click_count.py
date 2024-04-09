# Generated by Django 5.0.4 on 2024-04-08 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortapp', '0006_support'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clickstats',
            name='click_count',
        ),
        migrations.AddField(
            model_name='url',
            name='click_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]