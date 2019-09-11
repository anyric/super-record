from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, UpdateView, DetailView, DeleteView, CreateView )
from stocks.models import Product
from .forms import SalesCreationForm, EditSalesForm
from .models import Sales

@method_decorator(login_required, name="dispatch")
class SalesListView(ListView):
    queryset = Sales.objects.all().order_by('-id')
    paginate_by = 10
    context_object_name = 'sales'
    template_name = 'sales/sales.html'

@method_decorator(login_required, name="dispatch")
class SalesCreationView(CreateView, ListView):
    model=Sales
    form_class = SalesCreationForm
    context_object_name = 'sales_list'
    object_list = []
    template_name = 'sales/add_sales.html'
    success_message = 'Success: Sales creation succeeded.'
    success_url = reverse_lazy('sale')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales'] = Sales.objects.filter(status='pending').filter(
            sold_by=self.request.user.id)
        context['total_sales'] = Sales.objects.filter(status='pending').filter(
            sold_by=self.request.user.id).aggregate(Sum('total_amount'))

        return context

    def post(self, request, *args, **kwargs):

        if request.method == 'POST' and request.POST.get('item'):
            sale = Product.objects.filter(id=request.POST.get('item')).values()[0]
            data = {
                'name': sale['name'],
                'item': int(request.POST.get('item')),
                'quantity': request.POST.get('quantity', 0),
                'unit_price': float(sale['unit_price']),
                'total_amount': float(int(request.POST.get('quantity', 0)) * float(
                    sale['unit_price'])),
                'sold_by': request.user.id
            }
            form = self.form_class(data)
            form.name=sale['name']
            form.unit_price=[]

            if form.is_valid():
                form.save()

                return HttpResponseRedirect(self.success_url)

        return super().post(request, *args, **kwargs)

@method_decorator(login_required, name="dispatch")
class EditSalesView(UpdateView, DetailView):
    template_name = 'sales/edit_sale.html'
    pk_url_kwarg = 'id'
    form_class = EditSalesForm
    queryset = Sales.objects.all()
    success_url = reverse_lazy('sale')

@method_decorator(login_required, name="dispatch")
class DeleteSalesView(DeleteView):
    template_name = 'sales/delete_sale.html'
    pk_url_kwarg = 'id'
    queryset = Sales.objects.all()
    success_url = reverse_lazy('sale')

@method_decorator(login_required, name="dispatch")
class CheckoutView(ListView):
    queryset = Sales.objects.all().order_by('-id')
    context_object_name = 'sales'
    template_name = 'sales/checkout.html'
    success_url = reverse_lazy('sale')
    item_list = []
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_sales'] = Sales.objects.filter(status='pending').filter(
            sold_by=self.request.user.id).aggregate(Sum('total_amount'))
        context['balance'] = float(0.0)
        self.item_list += Sales.objects.filter(status='pending').values()

        return context

    def post(self, request, *args, **kwargs):

        if request.method == 'POST' and request.POST.get('total_amount') and request.POST.get('amount_received'):
            Sales.objects.filter(status='pending').filter(
                sold_by=request.user.id).update(status='sold')
            for item in self.item_list:
                prod = Product.objects.get(name=item['name'])
                stock_balance = prod.stock_level - item['quantity']
                Product.objects.filter(name=item['name']).update(stock_level=stock_balance)

            return HttpResponseRedirect(self.success_url)

        return render(request, self.template_name)