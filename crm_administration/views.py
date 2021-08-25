from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.decorators import allowed_users


def loading_page(request):
    return render(request, 'crm_administration/loading_page.html')


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin', 'user'])
def dashboard(request):
    return render(request, 'crm_administration/dashboard.html')
