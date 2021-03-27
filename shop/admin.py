from django.contrib import admin

# Register your models here.
from shop.models import *


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)
