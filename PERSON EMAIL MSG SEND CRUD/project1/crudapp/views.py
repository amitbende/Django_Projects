from email import message
import email
from django.shortcuts import render, redirect
from .forms import ResumeForm
from .models import Resume
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
@login_required(login_url='login_url')
def Resume_View(request):
    form = ResumeForm()
    template_name = 'crudapp/resumeform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showresume_url')
    return render(request, template_name, context)

@login_required(login_url='login_url')
def ShowResume_View(request, page=1):
    data = Resume.objects.all()
    template_name = 'crudapp/showresume.html'
    
    paginator = Paginator(data,1)
    try:
        data = paginator.page(page)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    context = {'obj': data}
    return render(request, template_name, context)

def UpdateResume_View(request, id):
    obj = Resume.objects.get(student_id = id)
    form = ResumeForm(instance = obj)
    template_name = 'crudapp/resumeform.html'
    context = {'form': form}
    if request.method == 'POST':
        print('line 32')
        form = ResumeForm(request.POST, instance = obj)
        if form.is_valid():
            print('line 35')
            form.save()
            return redirect('showresume_url')
    return render(request, template_name, context)

def DeleteResume_View(request, id):
    obj = Resume.objects.get(student_id = id)
    template_name = 'crudapp/confirmation.html'
    context = {'obj': obj}
    if request.method == 'POST':
        obj.delete()
        return redirect('showresume_url')
    return render(request, template_name, context)

def Send_Email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        send_mail(
    'Hello, AMIT BENDE, Using Django Email Service',
    message,
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False )

    template_name = 'crudapp/email.html'
    return render(request, template_name)

'''
def signup(request):
    template_name = 'crudapp/email.html'
    context = {}
    subject = 'Hello, You Are Using Django Email'
    message = f'Hi, Thanku You For Connecting Us...'
    email_from = settings.EMAIL_HOST_USER,
    recipient_list = [request.POST.get('email')]
    if request.method == "POST":
        send_mail(subject, message, email_from, recipient_list)
    return render(request, template_name, context)'''