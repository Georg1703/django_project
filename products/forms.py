from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    """ Form to add factory """
    class Meta:
        model = Product
        fields = '__all__'