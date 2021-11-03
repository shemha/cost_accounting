from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from users.forms import CustomUserCreationForm
from .forms import *
from .models import *
from django.views.generic import ListView, View


# Create your views here.
# def base_branch(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     return render(request, 'app/base.html', {'user': user})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            input_email = form.cleaned_data['email']
            input_password = form.cleaned_data['password1']
            new_user = authenticate(
                email=input_email,
                password=input_password,
            )
            if new_user is not None:
                login(request, new_user)
                return redirect('costs:warehousing')
    else:
        form = CustomUserCreationForm()
        return render(request, 'costs/signup.html', {'form': form})


def warehousing(request):
    if request.method == "POST":
        form = WarehousingForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
    else:
        form = WarehousingForm(request.POST)
        context = {'form': form}
    return render(request, 'costs/warehousing.html', context)


def warehousing_views(request, filter):
    warehousing = Warehousing.objects.order_by(filter)
    context = {'warehousing': warehousing}
    return render(request, 'costs/warehousing_views.html', context)


def cost_accounting(request):
    if request.method == "POST":
        form = CostForm(request.POST)
        context = {'form': form,}
        if form.is_valid():
            form.save()
    else:
        form = CostForm(request.POST)
        context = {'form': form,}
    return render(request, 'costs/cost_accounting.html', context)


def cost_views(request, filter):
    costs = Cost.objects.order_by(filter)
    context = {'costs': costs}
    return render(request, 'costs/cost_views.html', context)


def profit(request):
    form = CostForm()
    context = {'form': form,}
    return render(request, 'costs/profit.html', context)


def earning(request):
    if request.method == "POST":
        form = SaleForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
    else:
        form = SaleForm(request.POST)
        context = {'form': form}
    return render(request, 'costs/earning.html', context)


def orderer_info(request):
    if request.method == "POST":
        form = OrdererForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
    else:
        form = OrdererForm(request.POST)
        context = {'form': form}
    return render(request, 'costs/orderer_info.html', context)


def customer_info(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
    else:
        form = CustomerForm(request.POST)
        context = {'form': form}
    return render(request, 'costs/customer_info.html', context)


def earning_views(request, filter):
    customer = Customer.objects.order_by(filter)
    orderer = Orderer.objects.order_by(filter)
    context = {'customer': customer, 'orderer': orderer }
    return render(request, 'costs/cost_views.html', context)