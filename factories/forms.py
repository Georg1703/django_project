from django.forms import ModelForm
from .models import Factory


class FactoryForm(ModelForm):
    """ Form to add factory """
    class Meta:
        model = Factory
        fields = ['name', 'link']