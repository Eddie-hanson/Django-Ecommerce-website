from django.db import models

# Create your models here.


class Category(models.Model):
    Name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.Name

# class Banner (models.Model):
#     Name=models.CharField(max_length=50)
#     Image=models.ImageField()


class Product(models.Model):

    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=250, default='Clothes')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(default='No description')
    size = models.CharField(
        max_length=12,  default='Size not available')
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
