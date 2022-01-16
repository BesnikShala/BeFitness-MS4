from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ A View to show all clothing products, sorting and search options """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)