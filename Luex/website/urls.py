from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='Home'),
    path('Products/', views.Products_Page, name='Products'),
    path('About/', views.About, name='about'),
    path('ProductDetails/<int:pk>', views.ProductDetails, name='ProductDetails'),
    path('cart/', views.CartPage, name='cart'),
    path('Search/', views.Search_Apparel, name='Search'),
    path('Categorylisting/<foo>/',
         views.Category_Product_listing, name='Categorylisting'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:pk>/',
         views.remove_from_cart, name='remove_from_cart'),
    path('Delete_from_cart/<int:pk>',
         views.Delete_from_cart, name="Delete_from_cart"),

]
