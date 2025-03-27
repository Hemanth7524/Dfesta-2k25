from django.db import models

# Create your models here.
class studentDetails(models.Model):
    fullname =  models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    dept = models.CharField(max_length=20)
    year = models.IntegerField()
    event = models.CharField(max_length=20)
    payment_verified = models.BooleanField(default=False)

class paymentDetails(models.Model):
    image = models.ImageField(upload_to="payment_images/")
    utr = models.TextField(unique=True)
    