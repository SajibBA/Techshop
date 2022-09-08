from django.db import models
from django.contrib.auth.models import AbstractUser , User


# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_details = models.TextField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    sub_category_name = models.CharField(max_length=100)
    sub_category_details = models.TextField(max_length=10000, null=True, blank=True)
    parent_category = models.ForeignKey(Category, related_name='parent_category', on_delete=models.CASCADE, )

    def __str__(self):
        return self.sub_category_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    brand_details = models.TextField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    name = models.CharField(max_length=100)
    product_pic = models.ImageField(upload_to='pics/', null=True, blank=True)
    product_details = models.TextField(max_length=10000, null=True, blank=True)
    normal_price = models.DecimalField( max_digits=8, decimal_places=2)
    discount_price = models.DecimalField( max_digits=8, decimal_places=2)
    has_discount = models.BooleanField(default=False)
    discount_amount = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)
    discount_percentage = models.DecimalField(null=True, blank=True, max_digits=3, decimal_places=2)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, )
    sub_category = models.ForeignKey(SubCategory, related_name='sub_category', on_delete=models.CASCADE, )
    brand = models.ForeignKey(Brand, related_name='brand', on_delete=models.CASCADE, )

    def __str__(self):
        return self.name


class CartProduct(models.Model):
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE, )
    buyer = models.ForeignKey(User, related_name='buyer', on_delete=models.CASCADE, )
    quantity = models.DecimalField( max_digits=8, decimal_places=0)
    unit_cost = models.DecimalField( max_digits=8, decimal_places=2)
    total_cost = models.DecimalField( max_digits=8, decimal_places=2)
