# Generated by Django 5.1.1 on 2025-03-18 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfestaapp', '0002_paymentdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdetails',
            name='image',
            field=models.ImageField(upload_to='media/payment_images'),
        ),
    ]
