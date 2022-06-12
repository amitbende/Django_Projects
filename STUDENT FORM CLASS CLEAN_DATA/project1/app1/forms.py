from django import forms

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

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    middle_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    mother_name = forms.CharField(max_length=50)
    date_of_birth = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    place_of_birth = forms.CharField(max_length=50)
    age = forms.IntegerField()
    gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=Gender))
    phone_number = forms.CharField()
    address = forms.CharField(max_length=100)
    email = forms.EmailField()
    Qualification = forms.CharField(label='Qualification', widget=forms.Select(choices=Qualification))
    language = forms.MultipleChoiceField(label='language', widget=forms.CheckboxSelectMultiple(),choices=Language)
    password = forms.CharField(max_length=50)