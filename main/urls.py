from django.urls import path
from main.views import product_list, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id

urlpatterns = [
    path('', product_list, name='product_list'),  # daftar produk
    path('create-product/', create_product, name='create_product'),  # buat produk baru
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),  # XML berdasarkan ID
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),  # JSON berdasarkan ID
]
