from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def homepage(request):
    return render(request, 'Home.html')

def About(request):
    return render(request, 'About.html')

def ProductDetails(request):
    return render(request, 'ProductDetails.html')    