from django.urls import path, include, re_path
from  . import  views
from .views import *


urlpatterns = [
     path('', views.home, name='home'),
     path('view_sub_category_products/<pk>/',
         views.view_sub_category_products, name='view_sub_category_products'),
     path('view_product_details/<pk>/',
         views.view_product_details, name='view_product_details'),
     re_path(r'^product$', searchproduct, name='searchproduct'),
     path('add_product_to_cart/<pk>/',
         views.add_product_to_cart, name='add_product_to_cart'),
     path('view_cart',
         views.view_cart, name='view_cart'),
     path('delete_product_from_cart/<pk>/',
         views.delete_product_from_cart, name='delete_product_from_cart'),


]