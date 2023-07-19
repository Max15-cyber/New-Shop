from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView
from .util import CategoryMixin
from django.db.models import Q

class ProductListView(ListView, CategoryMixin):
    model = Product

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')
        if search_query:
            return self.model.objects.filter(
                Q(product_name__icontains=search_query)
                |
                Q(product_description__icontains=search_query)
            )
        return self.model.objects.all()


class ProductDetailView(DetailView, CategoryMixin):
    model = Product
    

class CategoryDetailView(DetailView, CategoryMixin):
    model = Category
    

def product_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        products = Product.objects.filter(
            Q(product_name__icontains=search_query)
            |
            Q(product_description__icontains=search_query)
        )
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'shop/product_list.html', context = {'product_list': products, 'category_list': categories})

def category_detail(request, pk):
    category = Category.objects.get(pk = pk)
    categories = Category.objects.all()
    return render(request, 'shop/category_detail.html', context = {'category': category, 'category_list': categories})

def product_detail(request, pk):
    product = Product.objects.get(pk = pk)
    categories = Category.objects.all()
    return render(request, 'shop/product_detail.html', context={'product': product, 'category_list': categories})

def save_order(request):
    product = Product.objects.get(pk=request.POST['product_id'])
    order = Order()
    order.name = request.POST['user_name']
    order.email = request.POST['user_email']
    order.product = product
    order.save()
    categories = Category.objects.all()
    return render(request, 'shop/order.html', context={'product': product, 'categories': categories})


