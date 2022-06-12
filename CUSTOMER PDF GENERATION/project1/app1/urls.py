from django.urls import path
from . import views

urlpatterns = [
    path('cv/', views.Customer_View, name='customer_url'),
    path('show/', views.Show_Customer, name='show_Customer_url'),

    path('up/<int:pk>/', views.UpdateCustomer.as_view(), name='update_url'),
    path('dp/<int:pk>/', views.DeleteCustomer.as_view(), name='delete_url'),
    
    path('file/', views.PDF_View, name='pdf_file'),
    path('file/<int:pk>/', views.PDF_Single_View, name='pdf_file')
]