# Generated by Django 3.2.5 on 2021-07-29 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_myaccount_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myaccount',
            name='username',
            field=models.CharField(default=models.EmailField(max_length=60, unique=True), max_length=30, unique=True),
        ),
    ]