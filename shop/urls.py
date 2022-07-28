from django.urls import path, include
from  . import  views
from .views import *


urlpatterns = [
     path('', views.home, name='home'),
     path('view_sub_category_products/<pk>/',
         views.view_sub_category_products, name='view_sub_category_products'),
     path('view_product_details/<pk>/',
         views.view_product_details, name='view_product_details'),
     path(r'^product$', searchproduct, name='searchproduct'),


]