# Generated by Django 5.0.4 on 2024-04-10 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortapp', '0009_alter_report_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='support',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('pending', 'Pending'), ('resolved', 'Resolved'), ('closed', 'Closed')], default='Open', max_length=20),
        ),
    ]
