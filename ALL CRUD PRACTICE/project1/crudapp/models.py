from distutils.command.upload import upload
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Employee(models.Model):
    
    student_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null = True)
    place_of_birth = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=100)
    email = models.EmailField()
    Qualification = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    c_password = models.CharField(max_length=50)
    picture = models.ImageField(upload_to = 'photos')
    document = models.FileField(upload_to = 'files')
    details = models.TextField()

class SingletonBaseModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class SiteSetting(SingletonBaseModel):
    site_name = models.CharField(max_length=100)
