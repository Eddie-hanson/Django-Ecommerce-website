from django.db import models
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    Name = models.CharField(max_length=250)

    def __str__(self):
        return self.Name


class Product(models.Model):
    SIZES_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'X Large'),
        ('2XL', '2X Large'),
    )
    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=250, default='Clothes')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(default='No description')
    size = models.CharField(
        max_length=50, choices=SIZES_CHOICES, default='Size not available')
    not_available = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, )
    stock = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default='Category not available')

    def __str__(self):

        return {self.name}


# class Order(models.Model):
#     pass
