from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, DeleteView
from bootstrap_modal_forms.generic import BSModalCreateView
from .forms import UserRegisterForm, EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .models import User

@method_decorator(login_required, name='dispatch')
class UserListView(ListView):
    queryset = User.objects.all().order_by('id')
    paginate_by = 7
    context_object_name = 'user_list'
    template_name = 'accounts/user.html'

@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView, DetailView):
    template_name = 'accounts/edit.html'
    pk_url_kwarg = 'id'
    form_class = EditProfileForm
    queryset = User.objects.all()
    success_url = reverse_lazy('setting')

@method_decorator(login_required, name='dispatch')
class PasswordUpdateView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    pk_url_kwarg = 'id'
    form_class = PasswordChangeForm
    queryset = User.objects.all()
    success_url = reverse_lazy('setting')

@method_decorator(login_required, name='dispatch')
class DeactivateView(DeleteView):
    template_name = 'accounts/deactivate.html'
    pk_url_kwarg = 'id'
    queryset = User.objects.all()
    success_url = reverse_lazy('setting')

class ActivateView(DeleteView):
    template_name = 'accounts/activate.html'
    pk_url_kwarg = 'id'
    queryset = User.objects.all()
    success_url = reverse_lazy('setting')

@method_decorator(login_required, name='dispatch')
class SignUpView(BSModalCreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/signup.html'
    success_message = 'Success: Sign up succeeded.'
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
def sales(request):
    return render(request, 'accounts/sales.html', {})

@login_required
def expense(request):
    return render(request, 'accounts/expense.html', {})

