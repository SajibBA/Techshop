from django.http import Http404
from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    product = Product.objects.all()
    brand = Brand.objects.all()
    category = Category.objects.all()
    sub_category = SubCategory.objects.all()

    context = {'product': product, 'brand': brand, 'category': category,
               'sub_category': sub_category, }
    return render(request, 'home.html', context)


def view_sub_category_products(request, pk):
    try:
        subCategory = SubCategory.objects.get(pk=pk)
    except SubCategory.DoesNotExist:
        raise Http404
    product = Product.objects.all()
    brand = Brand.objects.all()
    category = Category.objects.all()
    sub_category = SubCategory.objects.all()
    product_in_this = Product.objects.filter(sub_category=subCategory)

    context = {'subCategory': subCategory, 'product': product,
               'brand': brand, 'category': category,
               'sub_category': sub_category, 'product_in_this': product_in_this}
    return render(request, 'sub_category_products.html', context)