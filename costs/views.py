from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, WarehousingForm
from .models import Product, Vender


# Create your views here.
def index(request):
    form = WarehousingForm()
    context = {'form': form,}
    return render(request, 'costs/index.html', context)


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
                return redirect('costs:index')
    else:
        form = CustomUserCreationForm()
        return render(request, 'costs/signup.html', {'form': form})


def detail(request, product_id, vender_id):
    product = get_object_or_404(Product, pk=product_id)
    vender = get_object_or_404(Vender, pk=vender_id)
    context = {'product': product, 'vender': vender}
    return render(request, 'costs/detail.html', context)
