from django.views.generic import TemplateView

class SalesListView(TemplateView):
    template_name = 'sales/sales.html'
