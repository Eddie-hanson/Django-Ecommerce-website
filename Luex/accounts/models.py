from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name',]

    def __str__(self):
        return f'{self.email} {self.first_name} {self.last_name}'


class User_Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='Profile_PICS')
    Digital_address = models.CharField(max_length=20, default='')
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=20, default='')
    Region = models.CharField(max_length=20, default='')
    City = models.CharField(max_length=20, default='')
    Town = models.CharField(max_length=20, default='')

    def __str__(self):
        return f"{self.user.username} - {self.user.email}"


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User_Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
