from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'Home.html')


def Cart(request):
    return render(request, 'cart.html')


def About(request):
    return render(request, 'About.html')


def ProductDetails(request):
    return render(request, 'ProductDetails.html')
