# Generated by Django 3.2.5 on 2021-07-30 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_remove_myaccount_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='myaccount',
            name='password',
            field=models.CharField(default='changeme', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]