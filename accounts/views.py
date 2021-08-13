from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages

from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin', 'user'])
def home(request):
    return render(request, 'accounts/home.html')


def loading_page(request):
    return render(request, 'accounts/loading_page.html')


@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            group = Group.objects.get(name='user')
            user.groups.add(group)

            messages.success(request, 'Account was created !')
            return redirect('accounts:login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def login_page(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('accounts:home')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'accounts/login.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('accounts:login')