from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    category = models.CharField(max_length=50)
    ingredients = models.TextField()
    allergen_warning = models.TextField()
    customizable = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
