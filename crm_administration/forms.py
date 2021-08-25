from django import forms
from django.forms import ModelForm
from .models import Factory, Deposit


class FactoryForm(ModelForm):
    """ Form to add factory """
    class Meta:
        model = Factory
        fields = '__all__'


class DepositForm(ModelForm):
    """ Form to add deposit """
    class Meta:
        model = Deposit
        fields = '__all__'
