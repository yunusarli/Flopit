from django.contrib import admin
from .models import (
    Category, 
    UserProfile,
    Product,
    Comment,
    Tag,
    ProductImage,
    Point,
    Basket,)

admin_list = [Category,UserProfile,Product,Comment,Tag,ProductImage,Point,Basket]

for al in admin_list:
    admin.site.register(al)