from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, User_Profile


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name',
                    'last_name')


# class ProfileAdmin(UserAdmin):
#     list_display = ('image', 'first_name', 'last_name', 'email')


admin.site.register(User, CustomUserAdmin),
admin.site.register(User_Profile)
