from django import forms
from .models import Employee
from django.core import validators

Gender = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
]

Qualification = [
    ('select', 'select'),
    ('M.Tech', 'M.Tech'),
    ('B.Tech', 'B.Tech'),
    ('MCA', 'MCA'),
    ('BCA', 'BCA')
]

Language = [
    ('select', 'select'),
    ('Python', 'Python'),
    ('Java', 'Java'),
    ('Ruby', 'Ruby'),
    ('Html', 'Html')
]

class EmployeeForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=Gender))
    Qualification = forms.CharField(label='Qualification', widget=forms.Select(choices=Qualification))
    language = forms.MultipleChoiceField(label='language', widget=forms.CheckboxSelectMultiple(), choices=Language)

    age = forms.IntegerField(validators=[validators.MinValueValidator(18), validators.MaxValueValidator(60)])

    class Meta:
        model = Employee
        fields = '__all__'

    
    def clean_first_name(self):
        value = self.cleaned_data['first_name']
        if value.istitle() != True:
            raise validators.ValidationError('First Character is Small !!!')
        return value

    # def clean_Qualification(self):
    #     value = self.cleaned_data['Qualification']
    #     if value < 0 or value > 2:
    #         raise validators.ValidationError('You Can not Select More than 2 field ')
    #     return value

    def clean(self):
        all_data = super().clean()
        pass1 = all_data['password']
        pass2 = all_data['c_password']
        if pass1 != pass2:
            raise validators.ValidationError('Password and C-Password are Different !!')
