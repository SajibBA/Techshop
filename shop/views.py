from unicodedata import category
from django.http import Http404
from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.

# Display all products.

def home(request):
    product = Product.objects.all()
    brand = Brand.objects.all()
    category = Category.objects.all()
    sub_category = SubCategory.objects.all()
    nonemty_sub_category = []
    for sub_categorys in  sub_category:
        for products in product:
            if sub_categorys == products.sub_category:
                nonemty_sub_category.append(sub_categorys)
                break

    context = {'product': product, 'brand': brand, 'category': category,
               'sub_category': sub_category, 'nonemty_sub_category' : nonemty_sub_category}
    return render(request, 'shop/home.html', context)

# Show selected categorys products

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
    brand_in_this = []
    for brands in  brand:
        for products in product_in_this:
            if brands == products.brand:
                brand_in_this.append(brands)
                break

    context = {'subCategory': subCategory, 'product': product,
               'brand': brand, 'category': category,
               'sub_category': sub_category, 'product_in_this': product_in_this,
               'brand_in_this': brand_in_this, }
    return render(request, 'shop/sub_category_products.html', context)



# Show details of the selected product

def view_product_details(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404
    brand = Brand.objects.all()
    category = Category.objects.all()
    sub_category = SubCategory.objects.all()
    context = {'product': product, 'brand': brand, 'category': category,
               'sub_category': sub_category, }
    return render(request, 'shop/product_details.html', context)



def searchproduct(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        brand = Brand.objects.all()
        product = Product.objects.all()
        category = Category.objects.all()
        sub_category = SubCategory.objects.all()
        nonemty_sub_category = []
        for sub_categorys in  sub_category:
            for products in product:
                if sub_categorys == products.sub_category:
                    nonemty_sub_category.append(sub_categorys)
                    break

        if query is not None:
            lookups= Q(name__icontains=query)

            product= Product.objects.filter(lookups).order_by('category').distinct()

            context={'product': product,
                    'submitbutton': submitbutton, 'brand': brand, 'category': category,
                    'sub_category': sub_category,'nonemty_sub_category' : nonemty_sub_category}

            return render(request, 'shop/search.html', context)

        else:
            return render(request, 'shop/search.html')

    else:
        return render(request, 'shop/search.html')
