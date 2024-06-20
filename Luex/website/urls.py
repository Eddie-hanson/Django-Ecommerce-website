from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.homepage, name='homepage'),
    path('About/', views.About, name='about'),
    path('ProductDetails/', views.ProductDetails, name='ProductDetails'),
           
]
