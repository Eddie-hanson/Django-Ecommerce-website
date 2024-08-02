from django.urls import path
from . import views

# app_name="Accounts"
urlpatterns = [
    path('', views.Register, name='Register'),
    path('Login', views.login_view, name='Login'),
    path('Logout', views.logout_view, name='Logout'),
]
