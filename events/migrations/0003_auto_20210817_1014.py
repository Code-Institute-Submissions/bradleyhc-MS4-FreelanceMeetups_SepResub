# Generated by Django 3.2.6 on 2021-08-17 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_registrants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='industry',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(default='Online', max_length=100),
        ),
    ]