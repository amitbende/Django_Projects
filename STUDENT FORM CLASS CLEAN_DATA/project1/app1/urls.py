from django.urls import path
from .import views

urlpatterns = [
    path('sf/', views.Student_view),
    path('ss/', views.ShowStudent_View)
]