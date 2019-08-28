from django.views.generic import (
    ListView, UpdateView, DetailView,
    DeleteView, CreateView, TemplateView
)

class Purchase(TemplateView):
    template_name = 'purchase/purchase.html'
