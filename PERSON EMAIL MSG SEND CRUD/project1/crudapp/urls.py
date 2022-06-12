from django.urls import path
from . import views

urlpatterns = [
    path('rf/', views.Resume_View, name='resumeform_url'),
    path('sr/', views.ShowResume_View, name='showresume_url'),
    path('sr/<int:page>/', views.ShowResume_View, name='showresume_url'),
    path('ur/<int:id>/', views.UpdateResume_View, name='update_url'),
    path('dr/<int:id>/', views.DeleteResume_View, name='delete_url'),
    path('sm/', views.Send_Email, name='email_url')
]