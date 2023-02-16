from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def product_list(request, pk = 0):
    if pk == 0:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(cat = pk)
    categories = Category.objects.all()
    return render(request, 'shop/products.html', context = {'products': products, 'categories': categories})

def product_detail(request, pk):
    product = Product.objects.get(pk = pk)
    categories = Category.objects.all()
    return render(request, 'shop/products_detail.html', context={'product': product, 'categories': categories})

def save_order(request):
    print(request.POST['product_id'])
    return render(request, 'shop/products.html')
