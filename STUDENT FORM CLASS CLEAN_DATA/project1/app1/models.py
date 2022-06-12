from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    phone_number = models.BigIntegerField()
    address = models.CharField(max_length=100)
    email = models.EmailField()
    Qualification = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

