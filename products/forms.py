from django.forms import ModelForm
from django import forms

from .models import Product, Category


class ProductForm(forms.Form):
    """ form to add product """
    non_formal_name = forms.CharField(label='Non formal name', max_length=100)


class CategoryForm(forms.Form):
    """" form to add category """
    name = forms.CharField(label='Category name', max_length=100)
    parent = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='No parent', required=False)

    