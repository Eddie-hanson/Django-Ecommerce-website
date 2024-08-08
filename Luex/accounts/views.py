from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from accounts.forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.conf import settings

# Reg_User = settings.AUTH_USER_MODEL
# Create your views here.


def Register(request):
    if request.method == 'POST':
        Registration = UserRegistrationForm(request.POST)

        if Registration.is_valid():
            new_user = Registration.save()
            # username = Registration.cleaned_data.get('username')
            # password = Registration.cleaned_data.get('password1')
            # messages.success(request, f'Account created for {username}!')
            # new_user = authenticate(
            #     username=Registration.cleaned_data['username'], password=Registration.cleaned_data['password1'])

            Email = Registration.cleaned_data.get('Email')
            password = Registration.cleaned_data.get('password1')
            messages.success(request, f'Account created for {Email}!')
            new_user = authenticate(
                username=Registration.cleaned_data['email'], password=Registration.cleaned_data['password1'])

            if new_user is not None:
                login(request, new_user)
                return redirect('Home')
            else:
                messages.error(
                    request, 'Authentication failed. Please try logging in.')
        else:
            messages.error(request, 'Registration failed. ')
    else:
        Registration = UserRegistrationForm()
    context = {'form': Registration}
    return render(request, 'Signup.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('Home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {user.username}!')
                return redirect('Home')
            else:
                messages.warning(request, 'Invalid Email or Password')
        except User.DoesNotExist:
            messages.warning(
                request, f' User with Email {email}  does not exist')

    return render(request, 'Login.html')


def logout_view(request):
    logout(request)

    messages.info(request, "You're logged Out!!")
    return redirect('Login')


def forgot_password(request):
    return render(request, "forgotpassword.html")
