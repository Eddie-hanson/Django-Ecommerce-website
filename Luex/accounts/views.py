from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import User, User_Profile
from accounts.forms import UserRegistrationForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.conf import settings

# Reg_User = settings.AUTH_USER_MODEL
# Create your views here.


def Register(request):
    if request.method == 'POST':
        Registration = UserRegistrationForm(request.POST)

        if Registration.is_valid():
            new_user = Registration.save()

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
    return render(request, 'SignUp.html', context)


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
                request.session['user'] = user.id
                request.session['email'] = email

                messages.success(request, f'Welcome {user.username}!')
                print('You are ', request.session['email'])
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


# @login_required
# def UserProfile(request):
#     try:
#         user_profile = User_Profile.objects.get(user=request.user)
#     except User_Profile.DoesNotExist:
#         user_profile = None
#     context = {'user_profile': user_profile}
#     # print('Your User profile is ', user_profile)
#     return render(request, "Profile.html", context)


# def edit_profile(request):
#     user_Profile = User_Profile.objects.get(user=request.user)
#     if request.method == 'POST':
#         form = UserProfileForm(
#             request.POST, request.FILES, instance=user_Profile)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             messages.success(request, 'Profile Updated successfully')
#             return redirect('profile')
#     else:
#         form = UserProfileForm(instance=user_Profile)
#     context = {'form': form,  'user_Profile':  user_Profile}
#     return render(request, 'editprofile.html', context)
