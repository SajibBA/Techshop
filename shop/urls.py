from django.urls import path, include
from  . import  views
from .views import *


urlpatterns = [
    path('', views.home, name='home'),
    path(r'view_sub_category_products/(?P<pk>\d+)/',
         views.view_sub_category_products, name='view_sub_category_products'),
    path(r'view_product_details/(?P<pk>\d+)/',
         views.view_product_details, name='view_product_details'),

]