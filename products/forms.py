from django.forms import ModelForm
from django import forms

from .models import Product, Category


class ProductForm(ModelForm):
    """ form to add product """
    class Meta:
        model = Product
        fields = ['name']


class CategoryForm(forms.Form):
    """" form to add category """
    name = forms.CharField(label='Category name', max_length=100)
    parent = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='No parent', required=False)

    