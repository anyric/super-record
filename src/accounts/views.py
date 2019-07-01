from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    form = UserLoginForm(request.POST or None)
    
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect('/')

    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def register_view(request, *args, **kwargs):
    form = UserRegisterForm(request.POST or None)
    
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return HttpResponseRedirect('accounts/login')

    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('accounts/login')



