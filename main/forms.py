from django import forms
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('Cake', 'Cake'),
        ('Bread', 'Bread'),
        ('Pastry', 'Pastry'),
        ('Cookies', 'Cookies')
    ]

    price = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter price'}))  
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)  

    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'stock', 'category', 'ingredients', 'allergen_warning', 'customizable']

def clean_price(self):
    price = self.cleaned_data.get('price')
    if not price.isdigit():
        raise forms.ValidationError("Price must be a number")
    
    # Convert the price to an integer
    return int(price)
def clean_name(self):
    name = self.cleaned_data["name"]
    return strip_tags(name)

def clean_description(self):
    description = self.cleaned_data["description"]
    return strip_tags(description)

def clean_ingredients(self):
    ingredients = self.cleaned_data["ingredients"]
    return strip_tags(ingredients)

def clean_allergen_warning(self):
    allergen_warning = self.cleaned_data["allergen_warning"]
    return strip_tags(allergen_warning)
