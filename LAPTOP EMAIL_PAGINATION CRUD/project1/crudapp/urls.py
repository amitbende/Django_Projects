from django.urls import path
from . import views

urlpatterns = [
    path('lf/', views.Laptop_View, name='laptop_url'),
    path('sl/', views.Showlaptop_View, name='showlaptop_url'),
    path('sl/<int:page>', views.Showlaptop_View, name='showlaptop_url'),
    path('ulp/<int:id>/', views.Update_view, name='update_url'),
    path('dl/<int:id>/', views.Delete_View, name='delete_url')
]