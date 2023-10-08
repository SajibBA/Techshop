from asyncio.windows_events import NULL
from unicodedata import category
from django.http import Http404
from .models import *
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# Display all products.

def home(request):
    product = Product.objects.all().order_by("sub_category")
    brand = Brand.objects.all()
    category = Category.objects.all()
    sub_category = SubCategory.objects.all()
    nonemty_sub_category = []


    paginator = Paginator(product, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    page = request.GET.get('page', 1)
    try:
        product = paginator.page(page)
        for sub_categorys in  sub_category:
            for products in product:
                if sub_categorys == products.sub_category:
                    nonemty_sub_category.append(sub_categorys)
                    break
    except PageNotAnInteger:
        product = paginator.page(1)
        for sub_categorys in  sub_category:
            for products in product:
                if sub_categorys == products.sub_category:
                    nonemty_sub_category.append(sub_categorys)
                    break
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
        for sub_categorys in  sub_category:
            for products in product:
                if sub_categorys == products.sub_category:
                    nonemty_sub_category.append(sub_categorys)
                    break
    context = {'product': product, 'brand': brand, 'category': category,
               'sub_category': sub_category, 'nonemty_sub_category' : nonemty_sub_category,
               "page_obj": page_obj}
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
    product_in_this = Product.objects.filter(sub_category=subCategory).order_by("brand")
    
    brand_in_this = []
    

    paginator = Paginator(product_in_this, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    page = request.GET.get('page', 1)
    try:
        product_in_this = paginator.page(page)
        for brands in  brand:
            for products in product_in_this:
                if brands == products.brand:
                    brand_in_this.append(brands)
                    break
        
    except PageNotAnInteger:
        product_in_this = paginator.page(1)
        for brands in  brand:
            for products in product_in_this:
                if brands == products.brand:
                    brand_in_this.append(brands)
                    break
        
    except EmptyPage:
        product_in_this = paginator.page(paginator.num_pages)
        for brands in  brand:
            for products in product_in_this:
                if brands == products.brand:
                    brand_in_this.append(brands)
                    break

    context = {'subCategory': subCategory, 'product': product,
               'brand': brand, 'category': category,
               'sub_category': sub_category, 'product_in_this': product_in_this,
               'brand_in_this': brand_in_this,"page_obj": page_obj }
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


# Search Product

def searchproduct(request):
    if request.method == 'GET':
        query= request.GET.get('q')         # Get the text from searchbar
        submitbutton= request.GET.get('submit')

        brand = Brand.objects.all()
        product = Product.objects.all()
        category = Category.objects.all()
        sub_category = SubCategory.objects.all()
        nonemty_sub_category = []

        if query is not None:
            if query == "":             # If search get empty or null value redirect homepage
                return redirect('home')
            lookups= Q(name__icontains=query)

            product= Product.objects.filter(lookups).order_by('category')

            for sub_categorys in  sub_category:
                for products in product:
                    if sub_categorys == products.sub_category:
                        nonemty_sub_category.append(sub_categorys)
                        break

            context={'product': product,
                    'submitbutton': submitbutton, 'brand': brand, 'category': category,
                    'sub_category': sub_category,'nonemty_sub_category' : nonemty_sub_category}

            return render(request, 'shop/search.html', context)

        else:
            return render(request, 'shop/home.html')

    else:
        return render(request, 'shop/home.html')


# Product adding to Cart

def add_product_to_cart(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404
    brand = Brand.objects.all()
    category = Category.objects.all()
    sub_category = SubCategory.objects.all()

    if request.user.is_authenticated:
        if request.POST:
                quantity = int(request.POST['quantity'])

                CartProduct.objects.get_or_create(
                    buyer=request.user,
                    product=product,
                    quantity=quantity,
                    unit_cost = product.discount_price,
                    total_cost = product.discount_price * quantity,
                )
                return redirect('view_cart')
    else:
        messages.error(request, "Please Login to add items in cart")

    context = {'product': product, 'brand': brand, 'category': category,
               'sub_category': sub_category, }
    return render(request, 'shop/adding_to_cart.html', context)



#Products added in cart so far

def view_cart(request):
    cartProduct = CartProduct.objects.filter(buyer=request.user)
    end_total_cost = 0
    for products in cartProduct:
        end_total_cost = end_total_cost + products.total_cost
    return render(request, 'shop/cart.html', {'cartProduct': cartProduct, 'end_total_cost': end_total_cost,})



# Delete selected product from cart

def delete_product_from_cart(request, pk):
    cartProduct = get_object_or_404(CartProduct, pk=pk)
    cartProduct.delete()
    return redirect("view_cart")