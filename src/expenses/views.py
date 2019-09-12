# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from django.urls import reverse_lazy
from django.views.generic import (
    # ListView, UpdateView, DetailView, DeleteView, CreateView,
    TemplateView)

@method_decorator(login_required, name="dispatch")
class ExpensesListView(TemplateView):
    template_name = 'expenses/expenses.html'
