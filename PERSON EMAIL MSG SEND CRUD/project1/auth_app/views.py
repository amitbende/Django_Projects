from hashlib import new
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.conf import settings
from django.core.mail import send_mail
from random import randint

otp = randint (1000,9999)

# Create your views here.
def Register_View(request):
    form = UserCreationForm()
    template_name = 'auth_app/register.html'
    context = {'form': form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, template_name, context)

def Login_views(request):
    template_name = 'auth_app/login.html'
    context = {}
    if request.method == 'POST':
        un = request.POST.get('u')
        pw = request.POST.get('p')

        global new
        user = authenticate(username=un, password=pw)
        new = user
        if user is not None:
            eml = request.POST.get('e')
            subject = 'Welcome to Django OTP Authentication'
            message = f'Hi{user.username}, {eml}, your otp is:{otp}, Thank You For Registeration'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [eml, 'bendeamitguruji@gmail.com']
            send_mail(subject, message, email_from, recipient_list)

            #login(request, user)
            return redirect('otp_url')
    return render(request, template_name, context)

def Logout_View(request):
    logout(request)
    return redirect('login_url')

def Otp_View(request):
    template_name = 'auth_app/otp.html'
    context = {}
    if request.method == 'POST':
        otp1 = int(request.POST.get('otp'))
        if otp == otp1:
            login(request, new)
            return redirect('showresume_url')
    return render(request, template_name, context)

