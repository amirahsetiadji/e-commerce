from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()  
    context = {
        'products': products,
        'name': 'Amirah Rizkita Setiadji',  
        'class_name': 'PBP B' 
    }
    return render(request, 'main.html', context)
