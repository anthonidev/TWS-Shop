from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Category

import random


def product_detail(request,category_slug,slug):
    product=get_object_or_404(Product,slug=slug)
    context={
        'product':product,
    }
    return render(request, 'product_detail.html', context)

def category_detail(request, slug):
    print("hola")
    category=get_object_or_404(Category,slug=slug)
    
    
    products=category.products.filter(parent=None)
    context={
        'category':category,
        'products':products,
    }
    return render(request, 'category_detail.html', context)