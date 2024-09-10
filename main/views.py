from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()  # Mengambil semua produk dari database
    context = {
        'products': products,
        'name': 'Amirah Rizkita Setiadji',  # Tambahkan nama
        'class_name': 'PBP B'  # Tambahkan kelas
    }
    return render(request, 'main.html', context)
