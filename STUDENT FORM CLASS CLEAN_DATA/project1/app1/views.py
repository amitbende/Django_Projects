from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student


# Create your views here.
def Student_view(request):
    form = StudentForm
    template_name = 'app1/studentform.html'
    context = {'form': form}
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            mother_name = form.cleaned_data['mother_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            place_of_birth = form.cleaned_data['place_of_birth']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            Qualification= form.cleaned_data['Qualification']
            language = form.cleaned_data['language']
            password = form.cleaned_data['password']

            s = Student(first_name=first_name, middle_name=middle_name, last_name=last_name, mother_name=mother_name,
                        date_of_birth=date_of_birth, place_of_birth=place_of_birth, age=age, gender=gender,
                        phone_number=phone_number, address=address, email=email, Qualification=Qualification,
                        language=language, password=password)
            s.save()

            return HttpResponse('<h1 style="color:green;"> Data Saved !!!</h1>')

    return render(request, template_name, context)

def ShowStudent_View(request):
    data = Student.objects.all()
    template_name = 'app1/showstudent.html'
    context = {'obj': data}
    return render(request, template_name, context)
