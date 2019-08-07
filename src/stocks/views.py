from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, UpdateView, DetailView, DeleteView, CreateView, TemplateView )
from .forms import ProductCreationForm, EditProductForm
from .models import Product
from decorators.decorators import group_required

decorators = [group_required(['Admin','Manager','General Manager'])]
@method_decorator(decorators, name="dispatch")
class ProductListView(ListView):
    query_set = Product.objects.all().order_by('id')
    paginate_by = 10
    context_object_name = 'product_list'
    template_name = 'stocks/product.html'


@method_decorator(decorators, name='dispatch')
class ProductCreationView(CreateView):
    form_class = ProductCreationForm
    template_name = 'stocks/add_product.html'
    success_message = 'Success: Product creation succeeded.'
    success_url = reverse_lazy('setting')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.stock_level = request.POST['quantity']
        form.created_by = request.user

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(self.success_url)

        return super().post(request, *args, **kwargs)


@method_decorator(decorators, name='dispatch')
class EditProductView(UpdateView, DetailView):
    template_name = 'stocks/edit_product.html'
    pk_url_kwarg = 'id'
    form_class = EditProductForm
    queryset = Product.objects.all()
    success_url = reverse_lazy('setting')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        prod = Product.objects.get(id=kwargs['id'])
        form.stock_level = request.POST['quantity']
        form.created_by = prod.created_by

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(self.success_url)
 
        return super().post(request, *args, **kwargs)


@method_decorator(decorators, name='dispatch')
class DeleteProductView(DeleteView):
    template_name = 'stocks/delete_product.html'
    pk_url_kwarg = 'id'
    queryset = Product.objects.all()
    success_url = reverse_lazy('setting')

