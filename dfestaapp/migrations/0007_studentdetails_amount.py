# Generated by Django 5.1.6 on 2025-03-20 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfestaapp', '0006_alter_paymentdetails_utr'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='amount',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
