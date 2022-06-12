from django.shortcuts import render,redirect
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CustomerForm
from .models import Customer
from django.http import FileResponse
from fpdf import FPDF

# Create your views here.
def Customer_View(request):
    template_name = 'app1/customer_form.html'
    form = CustomerForm()
    context = {'form':form}
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_Customer_url')
    return render(request, template_name, context)

def Show_Customer(request):
    template_name = 'app1/customer_list.html'
    data = Customer.objects.all()
    context = {'object_list':data}
    return render(request, template_name, context)

class UpdateCustomer(UpdateView):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('show_Customer_url')
    context_object_name = 'object_list'

class DeleteCustomer(DeleteView):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('show_Customer_url')
    context_object_name = 'object_list'

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

    farm = Customer.objects.all()

    for f in farm:
        lines.append(f.cid)
        lines.append(f.cname)
        lines.append(f.phone_number)
        lines.append(f.medicine)
        lines.append(f.cbill)
        lines.append(f.date)
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

    farm = Customer.objects.get(id = pk)
    ID = farm.cid
    NM = farm.cname
    PN = farm.phone_number
    MD = farm.medicine
    BI = farm.cbill
    DT = farm.date
    lines = [ID, NM, PN, MD, BI, DT]


    for line in lines:
        pdf.cell(200, 8, f"{line}", 0, 1)
    pdf.output(f'{NM}.pdf', 'F')
    return FileResponse(open(f'{NM}.pdf', 'rb'), as_attachment=True, content_type='application/pdf')

    