from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views import View
from bootstrap_modal_forms.generic import BSModalCreateView
from .forms import UserRegisterForm

@method_decorator(login_required, name='dispatch')
class SignUpView(BSModalCreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('setting')

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

