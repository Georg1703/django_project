from django.forms import ModelForm
from .models import Product, Category


class ProductForm(ModelForm):
    """ Form to add product """
    class Meta:
        model = Product
        fields = ['name']


class CategoryForm(ModelForm):
    """" for to add category """

    class Meta:
        model = Category
        fields = ['name']