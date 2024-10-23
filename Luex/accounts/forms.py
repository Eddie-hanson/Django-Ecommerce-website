from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User_Profile
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


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'section', 'type': 'text', 'placeholder': 'First Name'}))

    last_name = forms.CharField(widget=forms.TimeInput(
        attrs={'class': 'section', 'type': 'text', 'placeholder': 'last Name'}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'section', 'type': 'email', 'placeholder': 'Email', }))

    class Meta:
        model = User_Profile
        fields = ('image', 'Digital_address',
                  'address', 'Region', 'City', 'Town', 'phone')
        widgets = {
            'Digital_address': forms.TextInput(attrs={'class': 'section', 'type': 'text', 'placeholder': 'Digital Address', 'required': "required"}),
            'address': forms.EmailInput(attrs={'class': 'section', 'type': 'text', 'placeholder': 'Street Name', 'required': "required"}),
            'Region': forms.TextInput(attrs={'class': 'section', 'type': "text", 'placeholder': 'Region', 'required': "required"}),
            'City': forms.TextInput(attrs={'class': 'section', 'type': "text", 'placeholder': 'City', 'required': "required"}),
            'Town': forms.TextInput(attrs={'class': 'section', 'type': "text", 'placeholder': 'Town', 'required': "required"}),
            'phone': forms.NumberInput(attrs={'class': 'input', 'type': "tel", 'placeholder': 'Telephone number', 'required': "required", }),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ('image', 'Digital_address',
                  'address', 'Region', 'City', 'Town', 'phone')
        widgets = {
            'Digital_address': forms.TextInput(attrs={'class': 'section', 'type': 'text', 'placeholder': 'Digital Address', 'required': "required"}),
            'address': forms.TextInput(attrs={'class': 'section', 'type': 'text', 'placeholder': 'Street Name', 'required': "required"}),
            'Region': forms.TextInput(attrs={'class': 'section', 'type': "text", 'placeholder': 'Region', 'required': "required"}),
            'City': forms.TextInput(attrs={'class': 'section', 'type': "text", 'placeholder': 'City', 'required': "required"}),
            'Town': forms.TextInput(attrs={'class': 'section', 'type': "text", 'placeholder': 'Town', 'required': "required"}),
            'phone': forms.TextInput(attrs={'class': 'section', 'type': "tel", 'placeholder': 'Town', 'required': "required"}),
        }
