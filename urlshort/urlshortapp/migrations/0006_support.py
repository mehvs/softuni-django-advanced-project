# Generated by Django 5.0.4 on 2024-04-08 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortapp', '0005_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
            ],
        ),
    ]
