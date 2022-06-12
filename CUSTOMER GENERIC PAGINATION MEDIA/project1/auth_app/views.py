from ast import Not
from email import message
from re import template
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def Register_View(request):
    form = UserCreationForm()
    template_name = 'auth_app/register.html'
    context = {'form':form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login_url')
    return render(request, template_name, context)

def login_View(request):
    template_name = 'auth_app/login.html'
    context = {}
    if request.method == 'POST':
        un = request.POST.get('u')
        pw = request.POST.get('p')

        user = authenticate(username = un, password = pw )
        if user is not None:
            login(request, user)
            return redirect('customer_url')
    return render(request, template_name, context)

def Logout_View(request):
    logout(request)
    return redirect('login_url')


