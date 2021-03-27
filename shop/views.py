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