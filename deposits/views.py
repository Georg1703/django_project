from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from .forms import DepositForm
from .models import Deposit


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def add_deposit(request):
    context = {}
    form = DepositForm()

    if request.method == 'POST':
        form = DepositForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Deposit was saved !')
            return redirect('/dashboard')
        else:
            messages.success(request, 'Error!')
            context = {'form': form}
            return render(request, 'deposits/add_deposit.html', context)
    else:
        context = {'form': form}
        return render(request, 'deposits/add_deposit.html', context)


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def update_deposit(request, pk):
    deposit = Deposit.objects.get(id=pk)
    form = DepositForm(instance=deposit)

    if request.method == 'POST':
        form = DepositForm(request.POST, instance=deposit)

        if form.is_valid():
            form.save()
            messages.success(request, 'Deposit was updated !')
            return redirect('/dashboard')

    context = {'form': form}
    return render(request, 'deposits/add_deposit.html', context)


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def delete_deposit(request, pk):
    deposit = Deposit.objects.get(id=pk)

    if request.method == 'POST':
        deposit.delete()
        messages.success(request, 'Deposit was successfully deleted !')
        return redirect('/dashboard')

    context = {'item': deposit}
    return render(request, 'deposits/delete_deposit.html', context)
