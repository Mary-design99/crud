from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'photo', 'email', 'password', 'mobile_number', 'date_of_birth')
        labels = {
            'name': 'Patient Name',
            'photo': 'Photo',
            'email': 'Email Address',
            'password': 'Password',
            'mobile_number': 'Phone Number',
            'date_of_birth': 'Date of Birth',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 0712345678'}),
            'date_of_birth': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'}),
        }
