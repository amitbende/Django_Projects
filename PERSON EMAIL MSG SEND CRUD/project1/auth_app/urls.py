from django.urls import path
from . import views


urlpatterns = [
    path('rf/', views.Register_View, name='register_url'),
    path('log/', views.Login_views, name='login_url'),
    path('lgo/', views.Logout_View, name='logout_url'),
    path('otp/', views.Otp_View, name='otp_url')
]               