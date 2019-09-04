from django.urls import path
from sales import views as sales_views

urlpatterns = [
    path('sales/', sales_views.SalesListView.as_view(), name='sales'),
]
