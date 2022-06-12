from django import forms
from .models import Laptop

ram =[
    ('8gb', '8GB'),
    ('12gb', '12GB'),
    ('16gb', '16GB')
]

seller =[
    ('lotus', 'Lotus'),
    ('reliance', 'Reliance'),
    ('city collection', 'City Collection'),
    ('trends', 'Trends')
]


class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'

        labels = {
            'laptop_id':'LAPTOP ID',
            'name':'NAME',
            'model':'MODEL',
            'brand':'BRAND',
            'ram':'RAM',
            'price':'PRICE',
            'date':'MANUFACTURING DATE',
            'phone_number':'PHONE NUMBER',
            'seller':'SELLER',
            'address':'ADDRESS'
            }

        widgets = {
            'laptop_id':forms.NumberInput(attrs={'placeholder':'Enter Laptop Id'}),
            'name':forms.TextInput(attrs={'placeholder':'Enetr Laptop Name'}),
            'model':forms.TextInput(attrs={'placeholder':'Enetr Model Name'}),
            'ram':forms.RadioSelect(choices=ram),
            'price':forms.NumberInput(attrs={'placeholder':'Enetr Laptop Price'}),
            'date':forms.DateInput(attrs={'type':'date'}),
            'seller':forms.CheckboxSelectMultiple(choices=seller),
            'address':forms.Textarea(attrs={'placeholder':'Enetr Shop Address','rows':3})
        }
