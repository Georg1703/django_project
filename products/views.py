from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.decorators import allowed_users
from .forms import ProductForm


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['manager', 'owner', 'admin'])
def add_product(request):
    """ add factory """
    context = {}
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Factory was saved !')
            return redirect('/dashboard')
        else:
            messages.success(request, 'Error!')
            context = {'form': form}
            return render(request, 'factories/add_factory.html', context)
    else:
        context = {'form': form}
        return render(request, 'factories/add_factory.html', context)
