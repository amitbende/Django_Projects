from urllib import request
from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage

# Create your views here.
class CustomerLIst(ListView):
    model = Customer
    paginate_by = 2

class AddCustomer(CreateView):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('showcustomer_url')

class UpdateCustomer(UpdateView):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('showcustomer_url')

class DeleteCustomer(DeleteView):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('showcustomer_url')
    context_object_name = 'object_list'