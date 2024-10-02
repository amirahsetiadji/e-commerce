from django import forms
from main.models import Product

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
