# Generated by Django 3.2.6 on 2021-08-15 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_myaccount_job_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myaccount',
            name='job_role',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]