from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your First Name',

    }))
    last_name=forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Last Name',

    }))
    email=forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Email Address',

    }))
    phone_number=forms.CharField(widget=forms.TextInput(attrs={
        
        'class': 'form-control',
        'placeholder': 'Enter Your Phone Number',

    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Please enter your password',
        'class': 'form-control'
    }))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control'
    }))

    
    class Meta:
        model = Account
        fields=['first_name', 'last_name','email','phone_number','password']

    def __init__(self,*args,**kwargs):
            super(RegistrationForm,self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data=super(RegistrationForm,self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')

        if password!=confirm_password:
            raise forms.ValidationError('Password does not match!')

