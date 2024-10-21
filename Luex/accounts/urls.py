from django.urls import path
from . import views

# app_name="Accounts"
urlpatterns = [
    path('', views.Register, name='Register'),
    path('Login', views.login_view, name='Login'),
    path('Logout', views.logout_view, name='Logout'),
    path('forgot_password', views.forgot_password, name='forgotPassword'),
    path('profile', views.UserProfile, name='profile'),
    path('edit-profile', views.edit_profile, name='Edit-profile'),
]
