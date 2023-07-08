from django import forms
from .models import Product



class ProductForm(forms.ModelForm):
    '''
    class to define project form
    '''
    class Meta:
        model = Product
        exlcude = []
        fields = ('name','price','digital','availability','description','image') 