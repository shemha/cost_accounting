from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from users.forms import CustomUserCreationForm
from .forms import *
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.views.generic import ListView


# Create your views here.
def base_branch(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'costs/base.html', {'user': user})


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
        if form.is_valid():
            form.save()
    form = WarehousingForm()
    context = {'form': form}
    return render(request, 'costs/warehousing.html', context)


# class WarehousingListView(ListView):
#     model = Warehousing
#     context_object_name = 'warehousings'
#     template_name = 'warehousing_view.html'

def warehousing_view(request):
    warehousings = Warehousing.objects.all()
    return render(request, 'costs/warehousing_view.html', {'warehousings': warehousings})


def cost_accounting(request):
    if request.method == "POST":
        form = CostForm(request.POST)
        if form.is_valid():
            form.save()
    form = CostForm()
    context = {'form': form}
    return render(request, 'costs/cost_accounting.html', context)


def cost_views(request, filter):
    costs = Cost.objects.order_by(filter)
    context = {'costs': costs}
    return render(request, 'costs/cost_views.html', context)


def profit(request):
    form = CostForm()
    context = {'form': form}
    return render(request, 'costs/profit.html', context)


def earning(request):
    if request.method == "POST":
        form_sale = SaleForm(request.POST)
        if form_sale.is_valid():
            form_sale.save()
    form_sale = SaleForm()
    context = {'form_sale': form_sale,}
    return render(request, 'costs/earning.html', context)


def customer_info(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    form = CustomerForm()
    context = {'form': form}
    return render(request, 'costs/customer_info.html', context)
    # redirect('costs:earning')


def orderer_info(request):
    if request.method == "POST":
        form = OrdererForm(request.POST)
        if form.is_valid():
            form.save()
    form = OrdererForm()
    context = {'form': form}
    return render(request, 'costs/orderer_info.html', context)
    # redirect('costs:earning')


def earning_views(request, filter):
    customer = Customer.objects.order_by(filter)
    orderer = Orderer.objects.order_by(filter)
    context = {'customer': customer, 'orderer': orderer }
    return render(request, 'costs/cost_views.html', context)