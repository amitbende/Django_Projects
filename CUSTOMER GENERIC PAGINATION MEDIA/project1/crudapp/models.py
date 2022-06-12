from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    product = models.CharField(max_length=50)
    price = models.FloatField()
    customer_image = models.ImageField()
    customer_file = models.FileField()
