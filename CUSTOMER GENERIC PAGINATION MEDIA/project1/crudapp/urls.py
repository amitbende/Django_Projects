from django.urls import path
from . import views

urlpatterns = [
    path('cf/', views.AddCustomer.as_view(), name = 'customer_url'),
    path('sc/', views.CustomerLIst.as_view(), name = 'showcustomer_url'),
    path('sc/<int:page>/', views.CustomerLIst.as_view(), name = 'showcustomer_url'),
    path('up/<int:pk>/', views.UpdateCustomer.as_view(), name = 'update_url'),
    path('dl/<int:pk>/', views.DeleteCustomer.as_view(), name = 'delete_url')
]