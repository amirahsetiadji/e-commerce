from django.urls import path
from main.views import product_list, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user

app_name = 'main'

urlpatterns = [
    path('', product_list, name='product_list'),  # daftar produk
    path('create-product/', create_product, name='create_product'),  # buat produk baru
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),  # XML berdasarkan ID
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),  # JSON berdasarkan ID
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
      path('logout/', logout_user, name='logout'),
]