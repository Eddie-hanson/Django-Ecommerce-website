from django.shortcuts import render, redirect
from .models import Product, Category
# Create your views here.


def home(request):
    CategoryItems = Category.objects.all()
    Apparel = Product.objects.all().order_by('?')
    context = {'CategoryItems': CategoryItems, 'Apparels': Apparel}
    return render(request, 'Home.html', context)


def Category_Product_listing(request, foo):
    foo = foo.replace('-', '')
    category = Category.objects.get(CID=foo)
    products = Product.objects.filter(category=category)
    context = {'Category': category, 'Products': products}
    return render(request, 'Category.html', context)


def Search_Apparel(request):
    if request.method == 'POST':
        Search = request.POST['Searched']

        Items = Product.objects.filter(name__icontains=Search,)
        context = {'Searched': Search, 'Item': Items}
        return render(request, 'Search_Apparel.html', context)
    else:
        return render(request, 'Search_Apparel.html')


def Products(request):
    Apparel = Product.objects.all().order_by('?')
    context = {'Apparels': Apparel}
    return render(request, 'Products.html', context)


def Cart(request):
    return render(request, 'cart.html')


def About(request):
    return render(request, 'About.html')


def ProductDetails(request, pk):

    Apparels = Product.objects.get(id=pk)

    context = {'Apparel': Apparels}
    return render(request, 'ProductDetails.html', context)
