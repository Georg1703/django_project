from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.decorators import allowed_users
from .forms import FactoryForm, DepositForm
from .models import Factory, Deposit


def loading_page(request):
    return render(request, 'crm_administration/loading_page.html')


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin', 'user', 'manager', 'owner'])
def dashboard(request):
    context = {
        'factory_list': Factory.objects.all(),
        'deposit_list': Deposit.objects.all()
    }

    return render(request, 'crm_administration/dashboard.html', context)


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def add_factory(request):
    context = {}
    form = FactoryForm()

    if request.method == 'POST':
        form = FactoryForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Factory was saved !')
            return redirect('/dashboard')
        else:
            messages.success(request, 'Error!')
            context = {'form': form}
            return render(request, 'crm_administration/add_factory.html', context)
    else:
        context = {'form': form}
        return render(request, 'crm_administration/add_factory.html', context)


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def update_factory(request, pk):

    factory = Factory.objects.get(id=pk)
    form = FactoryForm(instance=factory)

    if request.method == 'POST':
        form = FactoryForm(request.POST, instance=factory)

        if form.is_valid():
            form.save()
            messages.success(request, 'Factory was updated !')
            return redirect('/dashboard')

    context = {'form': form}
    return render(request, 'crm_administration/add_factory.html', context)


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def delete_factory(request, pk):
    factory = Factory.objects.get(id=pk)

    if request.method == 'POST':
        factory.delete()
        messages.success(request, 'Factory was successfully deleted !')
        return redirect('/dashboard')

    context = {'item': factory}
    return render(request, 'crm_administration/delete_factory.html', context)


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def add_deposit(request):
    context = {}
    form = DepositForm()

    if request.method == 'POST':
        form = FactoryForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Factory was saved !')
            return redirect('/dashboard')
        else:
            messages.success(request, 'Error!')
            context = {'form': form}
            return render(request, 'crm_administration/add_deposit.html', context)
    else:
        context = {'form': form}
        return render(request, 'crm_administration/add_deposit.html', context)
