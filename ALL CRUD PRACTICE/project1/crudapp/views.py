from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage

from django.conf import settings
from django.core.mail import send_mail

from django.http import FileResponse
from fpdf import FPDF

# Create your views here.
@login_required(login_url='login_url')
def ShowHome_View(request):
    template_name = 'crudapp/home.html'
    context = {}
    return render(request, template_name, context)

@login_required(login_url='login_url')
def Employee_View(request):
    form = EmployeeForm()
    template_name = 'crudapp/employee.html'
    context = {'form': form}
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showemployee_url')
    return render(request, template_name, context)

@login_required(login_url='login_url')
def ShowEmployee_View(request, page=1):
    data = Employee.objects.all()
    template_name = 'crudapp/showemployee.html'

    paginator = Paginator(data,1)
    try:
        data = paginator.page(page)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
        
    context = {'obj': data}
    return render(request, template_name, context)

def UpdateEmployee_View(request, id):
    obj = Employee.objects.get(student_id = id)
    form = EmployeeForm(instance = obj)
    template_name = 'crudapp/employee.html'
    context = {'form': form}
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
            return redirect('showemployee_url')
    return render(request, template_name, context)

def DeleteEmployee_View(request, id):
    obj = Employee.objects.get(student_id = id)
    template_name = 'crudapp/confirmation.html'
    context = {'obj': obj}
    if request.method == 'POST':
        obj.delete()
        return redirect('showemployee_url')
    return render(request, template_name, context)

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        send_mail (
        'Hello, AMIT BENDE, Using Django Email Service',
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False )

    template_name = 'crudapp/email.html'
    return render(request, template_name)

def PDF_View(request):

    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('courier', 'B', 16)
    pdf.cell(40, 10, 'This is what you have sold this month so far:',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('courier', '', 12)
    pdf.cell(200, 8, f"{'Item'.ljust(30)} {'Amount'.rjust(20)}", 0, 1)
    pdf.line(10, 30, 150, 30)
    pdf.line(10, 38, 150, 38)

    lines = []

    farm = Employee.objects.all()

    for f in farm:
        lines.append(f.student_id)
        lines.append(f.first_name)
        lines.append(f.middle_name)
        lines.append(f.last_name)
        lines.append(f.mother_name)
        lines.append(f.date_of_birth)
        lines.append(f.place_of_birth)
        lines.append(f.time)
        lines.append(f.age)
        lines.append(f.gender)
        lines.append(f.phone_number)
        lines.append(f.address)
        lines.append(f.email)
        lines.append(f.Qualification)
        lines.append(f.language)
        lines.append(f.picture)
        lines.append(f.document)
        lines.append(f.details)
        lines.append(f.password)
        lines.append(' ')

    for line in lines:
        pdf.cell(200, 8, f"{line}", 0, 1)
    pdf.output('report.pdf', 'F')
    return FileResponse(open('report.pdf', 'rb'), as_attachment=True, content_type='application/pdf')

    
def PDF_Single_View(request, pk):

    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('courier', 'B', 16)
    pdf.cell(40, 10, 'This is what you have sold this month so far:',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('courier', '', 12)
    pdf.cell(200, 8, f"{'Item'.ljust(30)} {'Amount'.rjust(20)}", 0, 1)
    pdf.line(10, 30, 150, 30)
    pdf.line(10, 38, 150, 38)

    farm = Employee.objects.get(student_id = pk)
    ID = farm.student_id
    FN = farm.first_name
    MN = farm.middle_name
    LN = farm.last_name
    MON = farm.mother_name
    DOB = farm.date_of_birth
    POB = farm.place_of_birth
    TM = farm.time
    PN = farm.phone_number
    AG = farm.age
    G = farm.gender
    ADD = farm.address
    EM = farm.email
    EDU = farm.Qualification
    LG = farm.language
    PIC = farm.picture
    DOC = farm.document
    DET = farm.details
    PS = farm.password
    lines = [ID, FN, MN, LN, MON, DOB, POB, TM, PN, AG, G, ADD, EM, EDU, LG, PIC, DOC, DET, PS]


    for line in lines:
        pdf.cell(200, 8, f"{line}", 0, 1)
    pdf.output(f'{FN}.pdf', 'F')
    return FileResponse(open(f'{FN}.pdf', 'rb'), as_attachment=True, content_type='application/pdf')



    

