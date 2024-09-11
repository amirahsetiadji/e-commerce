from django.test import TestCase, Client
from django.utils import timezone
from .models import Product

class SweetBitesTest(TestCase):
    def setUp(self):
        # Menambahkan data produk untuk pengujian
        self.product1 = Product.objects.create(
            name="Red Velvet Cake",
            price=150000,
            description="A delicious Red Velvet Cake with cream cheese frosting.",
            stock=10,
            category="Cake",
            customizable=True,
            date_added=timezone.now()
        )
        self.product2 = Product.objects.create(
            name="Chocolate Croissant",
            price=75000,
            description="A crispy croissant filled with rich chocolate.",
            stock=20,
            category="Pastry",
            customizable=False,
            date_added=timezone.now()
        )

    def test_main_url_is_exist(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_product_str_representation(self):
        self.assertEqual(str(self.product1), "Red Velvet Cake")
        self.assertEqual(str(self.product2), "Chocolate Croissant")

    def test_product_customizable(self):
        self.assertTrue(self.product1.customizable)
        self.assertFalse(self.product2.customizable)
