from django.shortcuts import render, redirect
from .models import Product, Category
# Create your views here.


def home(request):
    CategoryItems = Category.objects.all()
    context = {'CategoryItems': CategoryItems}
    return render(request, 'Home.html', context)


def Cart(request):
    return render(request, 'cart.html')


def Search_Apparel(request):
    if request.method == 'POST':
        Search = request.POST['Searched']

        Items = Product.objects.filter(name__icontains=Search,)
        context = {'Searched': Search, 'Item': Items}
        return render(request, 'Search_Apparel.html', context)
    else:
        return render(request, 'Search_Apparel.html')


def Products(request):
    Apparel = Product.objects.all()
    context = {'Apparels': Apparel}
    return render(request, 'Products.html', context)


def About(request):
    return render(request, 'About.html')


def ProductDetails(request, pk):

    Apparels = Product.objects.get(id=pk)

    context = {'Apparel': Apparels}
    return render(request, 'ProductDetails.html', context)
