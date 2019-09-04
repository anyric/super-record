from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, UpdateView, DetailView, DeleteView, CreateView )
from .forms import ProductCreationForm, EditProductForm
from .models import Product
from decorators.decorators import group_required

decorators = [group_required(['Admin','Manager','General Manager'])]
@method_decorator(decorators, name="dispatch")
class ProductListView(ListView):
    queryset = Product.objects.all().order_by('id')
    paginate_by = 10
    context_object_name = 'product_list'
    template_name = 'stocks/products.html'

@method_decorator(decorators, name='dispatch')
class ProductCreationView(CreateView):
    form_class = ProductCreationForm
    template_name = 'stocks/add_product.html'
    success_message = 'Success: Product creation succeeded.'
    success_url = reverse_lazy('setting')

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.POST.get('name', None),
            'description': request.POST.get('description', None),
            'quantity': request.POST.get('quantity', 0),
            'unit_price': request.POST.get('unit_price', 0),
            'stock_level': request.POST.get('quantity', 0),
            'created_by': request.user.id
        }
        if request.method == 'POST':
            form = self.form_class(data)

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


@method_decorator(decorators, name='dispatch')
class DeleteProductView(DeleteView):
    template_name = 'stocks/delete_product.html'
    pk_url_kwarg = 'id'
    queryset = Product.objects.all()
    success_url = reverse_lazy('setting')

