from django import forms
from django.contrib.auth import models
from .models import Tutor_Profile,Student
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class create_user_form(forms.ModelForm):
    phone_number=forms.CharField(
        label="phone_number",
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'text', 'align':'center', 'placeholder':'phone_number'}),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':' Confirm password'}),
    )
    class Meta:
        model=User
        fields=['username','email']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'type':'text', 'align':'center', 'placeholder':'username'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'type':'email', 'align':'center', 'placeholder':'email'}),

        }


    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number'].lower()
        r = User.objects.filter(phone_number=phone_number)
        if r.count():
            raise  ValidationError("Phone number already exists")
        return phone_number
    
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['phone_number'],
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
          
        )
        return user

class Tutor_profile_form(forms.ModelForm):
    class Meta:
        model=Tutor_Profile
        exclude=('user',)
        


class Student_form(forms.ModelForm):
    class Meta:
        model=Student
        exclude=('Tutor',)
