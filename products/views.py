from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.decorators import allowed_users
from .forms import ProductForm, CategoryForm
from .models import ProductLang


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['manager', 'owner', 'admin'])
def add_product(request):
    """ add product """
    context = {}
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Product was saved !')
            return redirect('/dashboard')
        else:
            messages.success(request, 'Error!')
            context = {'form': form}
            return render(request, 'products/add_product.html', context)
    else:
        product_lang = ProductLang.objects.all()
        context = {'form': form, 'product_lang': product_lang}
        return render(request, 'products/add_product.html', context)


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['manager', 'owner', 'admin'])
def add_category(request):
    """ add category """
    context = {}
    form = CategoryForm()

    if request.method == 'POST':
        
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Category was saved !')
            return redirect('/dashboard')
        else:
            messages.success(request, 'Error!')
            context = {'form': form}
            return render(request, 'products/add_category.html', context)
    else:
        context = {'form': form}
        return render(request, 'products/add_category.html', context)
