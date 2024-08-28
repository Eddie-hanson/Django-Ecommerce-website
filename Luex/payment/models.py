from django.db import models
from accounts.models import User
from website.models import Product
from shortuuid.django_fields import ShortUUIDField
# Create your models here.


# class Order(models.Model):
#     ORDERED = 'Ordered'
#     STATUS_CHOICES = (
#         ('ORDERED', 'Ordered'),
#         ('DELIVERED', 'Delivered')
#     )

#     User = models.ForeignKey(User, on_delete=models.CASCADE)
#     order_id = ShortUUIDField(unique=True, length=10,
#                               max_length=15, prefix='ID')
#     first_name = models.CharField(max_length=90)
#     last_name = models.CharField(max_length=90)
#     email = models.EmailField()
#     phone = models.CharField(max_length=20, default='')
#     Digital_address = models.CharField(max_length=20, default='')
#     Region = models.CharField(max_length=20, default='')
#     paid = models.BooleanField(default=False)
#     Status = models.CharField(
#         max_length=250, choices=STATUS_CHOICES, default=ORDERED)
#     created_at = models.DateTimeField(auto_now_add=True)
#     Total_cost = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"{self.order_id} - {self.first_name} {self.last_name}. Total: {self.Total_cost} Status: {self.Status}"


# class Order_Item(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     price = models.IntegerField(max_digits=10, decimal_places=2, default=0.00)
#     quantity = models.IntegerField()

#     def __str__(self):
#         return f"{self.product.name} - {self.quantity} - {self.order.order_id}"
