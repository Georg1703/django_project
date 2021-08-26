from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from factories.models import Factory
from deposits.models import Deposit


def loading_page(request):
    return render(request, 'crm_administration/loading_page.html')


@login_required(login_url='accounts:login')
def dashboard(request):
    """ return rendered dashboard with factory and deposit lists """
    context = {
        'factory_list': Factory.objects.filter(is_active=True),
        'deposit_list': Deposit.objects.filter(is_active=True)
    }

    return render(request, 'crm_administration/dashboard.html', context)
