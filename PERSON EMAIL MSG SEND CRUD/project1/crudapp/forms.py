from django import forms
from .models import Resume

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

class ResumeForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=Gender))
    Qualification = forms.CharField(label='Qualification', widget=forms.Select(choices=Qualification))
    language = forms.MultipleChoiceField(label='language', widget=forms.CheckboxSelectMultiple(), choices=Language)

    class Meta:
        model = Resume
        fields = '__all__'