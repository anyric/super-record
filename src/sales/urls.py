from django.urls import path
from sales import views as sales_views

urlpatterns = [
    path('sales/', sales_views.SalesListView.as_view(), name='sales'),
    path('sale/', sales_views.SalesCreationView.as_view(), name='sale'),
    path('edit_sale/<int:id>/', sales_views.EditSalesView.as_view(), name='edit_sale'),
    path('delete_sale/<int:id>/', sales_views.DeleteSalesView.as_view(), name='delete_sale'),
]
