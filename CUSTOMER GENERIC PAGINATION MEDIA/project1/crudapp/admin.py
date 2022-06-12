from django.contrib import admin

from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'name', 'phone_number', 'product', 'price', 'customer_image', 'customer_file']

admin.site.register(Customer, CustomerAdmin)
