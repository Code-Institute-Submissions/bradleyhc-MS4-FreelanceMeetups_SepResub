# Generated by Django 3.2.5 on 2021-07-17 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_myaccount_stripe_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myaccount',
            name='stripe_customer_id',
            field=models.CharField(default='', max_length=50, null=True, unique=True),
        ),
    ]
