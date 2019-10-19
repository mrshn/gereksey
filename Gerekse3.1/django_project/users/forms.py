from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from blog.choices import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=10)
    site_kullanım_şartlarını_okudum_ve_kabul_ediyorum = forms.BooleanField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'site_kullanım_şartlarını_okudum_ve_kabul_ediyorum']
    

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
 
