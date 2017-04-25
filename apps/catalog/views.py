from django.shortcuts import render
from apps.catalog.models import Product


def products(request):
    products = Product.objects.all()
    return render(request, 'catalog.html', {'products': products})
