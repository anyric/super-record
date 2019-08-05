from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, UpdateView, DetailView, DeleteView, CreateView, TemplateView )
from decorators.decorators import group_required

decorators = [group_required(['Admin','Manager','General Manager'])]
@method_decorator(decorators, name="dispatch")
class Product(TemplateView):
    template_name = 'stocks/product.html'
