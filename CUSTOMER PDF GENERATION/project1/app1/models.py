from django.db import models

# Create your models here.
class Customer(models.Model):
    cid = models.IntegerField()
    cname = models.CharField(max_length=20)
    phone_number = models.BigIntegerField()
    medicine = models.CharField(max_length=20)
    cbill = models.FloatField()
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.cid}...{self.cname}...{self.bill}'