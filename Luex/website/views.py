from django.shortcuts import render, redirect
from .models import Product, Category
# Create your views here.


def home(request):
    Items = Product.objects.all()
    context = {Items: 'Items'}
    return render(request, 'Home.html', context)


def Cart(request):
    return render(request, 'cart.html')


def About(request):
    return render(request, 'About.html')


def ProductDetails(request):
    # try:
    #     Item = Product.objects.get()
    # except Item.DoesNotExist:
    #     return redirect('Home')
    return render(request, 'ProductDetails.html')
