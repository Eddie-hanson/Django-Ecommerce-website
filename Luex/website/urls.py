from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='Home'),
    path('Products/', views.Products, name='Products'),
    path('About/', views.About, name='about'),
    path('ProductDetails/<int:pk>', views.ProductDetails, name='ProductDetails'),
    path('cart/', views.Cart, name='cart'),
    path('Search/', views.Search_Apparel, name='Search'),

]
