from django import forms
from .models import Product

class ProductCreationForm(forms.ModelForm):
    """
    A form for creating new product with all required field
    """
    stock_level = forms.IntegerField(label='stock level', widget=forms.IntegerField)
    created_by = forms.IntegerField(label='created by', widget=forms.IntegerField)

    class Meta:
        model = Product
        fields = ('name', 'description', 'quantity', 'unit_price')

class EditProductForm(forms.ModelForm):
    """
    A form for editing existing product with all required field
    """
    stock_level = forms.IntegerField(label='stock level', widget=forms.IntegerField)
    created_by = forms.IntegerField(label='created by', widget=forms.IntegerField)

    class Meta:
        model = Product
        fields = ['name', 'description', 'quantity', 'unit_price']
