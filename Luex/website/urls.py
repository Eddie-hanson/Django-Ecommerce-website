from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='Home'),

    path('About/', views.About, name='about'),
    path('ProductDetails/', views.ProductDetails, name='ProductDetails'),
    path('cart/', views.Cart, name='cart'),

]
