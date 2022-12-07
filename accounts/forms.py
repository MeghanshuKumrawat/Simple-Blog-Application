from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User

class User_Creation_Form(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-4"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-4"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-4"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-4"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-4"}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class User_Change_Form(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-4"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-4"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-4"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control mb-4"}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        


class Login_Form(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-4"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-4"}))