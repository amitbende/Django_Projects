from django.urls import path
from . import views 

urlpatterns = [
    path('hv/', views.ShowHome_View, name='home_url'),
    path('ef/', views.Employee_View, name='employee_url'),

    path('er/', views.ShowEmployee_View, name='showemployee_url'),

    path('er/<int:page>', views.ShowEmployee_View, name='showemployee_url'),

    path('ur/<int:id>', views.UpdateEmployee_View, name='update_url'),
    path('dr/<int:id>', views.DeleteEmployee_View, name='delete_url'),

    path('sup/', views.signup, name='signup_url'),
    
    path('file/', views.PDF_View, name='pdf_file'),
    path('file/<int:pk>/', views.PDF_Single_View, name='pdf_file')
]