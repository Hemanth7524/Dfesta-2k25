# Generated by Django 5.1.1 on 2025-03-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfestaapp', '0005_studentdetails_payment_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdetails',
            name='utr',
            field=models.TextField(unique=True),
        ),
    ]
