from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input', 'type': 'password', 'placeholder': 'Password', 'required': "required"}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input', 'type': 'password', 'placeholder': 'Confirm Password', 'required': "required"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',]
        widgets = {'first_name': forms.TextInput(attrs={'class': 'input', 'type': 'text', 'placeholder': 'First Name', 'required': "required"}),
                   'last_name': forms.TextInput(attrs={'class': 'input', 'type': 'text', 'placeholder': 'Last Name', 'required': "required"}),
                   'email': forms.EmailInput(attrs={'class': 'input', 'type': 'text', 'placeholder': 'Email', 'required': "required"}),
                   'username': forms.TextInput(attrs={'class': 'input', 'type': "text", 'placeholder': 'Username', 'required': "required"}),
                   }
