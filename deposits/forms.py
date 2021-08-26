from django.forms import ModelForm
from .models import Deposit


class DepositForm(ModelForm):
    """ Form to add deposit """
    class Meta:
        model = Deposit
        fields = '__all__'
