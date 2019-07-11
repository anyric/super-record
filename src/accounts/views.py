from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

@login_required
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def home(request):
    return render(request, 'accounts/home.html', {})

@login_required
def product(request):
    return render(request, 'accounts/product.html', {})

@login_required
def purchase(request):
    return render(request, 'accounts/purchase.html', {})

@login_required
def setting(request):
    return render(request, 'accounts/setting.html', {})

@login_required
def user(request):
    return render(request, 'accounts/user.html', {})

@login_required
def sales(request):
    return render(request, 'accounts/sales.html', {})

@login_required
def expense(request):
    return render(request, 'accounts/expense.html', {})

