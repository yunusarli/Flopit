from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from main.models import Point, Product, ProductImage

def index(request):
    products = Product.objects.all().order_by("-created")
    p_with_points = list()
    
    for product in products:
        points = Point.objects.filter(product=product)
        
        if points:
            total = 0
            for point in points:
                total += point.value
            avg = float(total/len(points))

        p_with_points.append({
            'product':product,
            'point':avg,
            'thumbnail':product.get_thumbnail(ProductImage)
            })

    return render(request,'index.html',{
        'products':p_with_points
    })


#detay sayfasına git ve orayı düzenle