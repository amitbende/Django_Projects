from django.urls import path
from . import views

urlpatterns = [
    path('rf/', views.Register_View, name='register_url'),
    path('log/', views.login_View, name='login_url'),
    path('lout/', views.Logout_View, name='logout_url')
]
