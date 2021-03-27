from django.db import models

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
    normal_price = models.IntegerField(max_length=100)
    discount_price = models.IntegerField(max_length=100)
    has_discount = models.BooleanField(default=False)
    discount_amount = models.IntegerField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, )
    sub_category = models.ForeignKey(SubCategory, related_name='sub_category', on_delete=models.CASCADE, )
    brand = models.ForeignKey(Brand, related_name='brand', on_delete=models.CASCADE, )

    def __str__(self):
        return self.name

