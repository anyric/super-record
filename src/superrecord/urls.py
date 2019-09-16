from django.urls import path, include
from django.contrib import admin
from . import views as main_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view.IndexView.as_view(), name='index'),
    path('reports/', main_view.AccountReportView.as_view(), name='reports'),
    path('reports/accounts/', main_view.AccountListView.as_view(), name='accounts'),
    path('reports/roles/', main_view.RolesListView.as_view(), name='roles'),
    path('reports/stocks/', main_view.StocksListView.as_view(), name='stocks'),
    path('reports/purchases/', main_view.PurchaseListView.as_view(), name='purchases'),
    path('reports/sales/', main_view.SalesListView.as_view(), name='sales'),
    path('reports/categories/', main_view.CategoryListView.as_view(), name='categories'),
    path('reports/expenses/', main_view.ExpensesListView.as_view(), name='expenses'),
    path('accounts/', include('accounts.urls')),
    path('stocks/', include('stocks.urls')),
    path('purchases/', include('purchase.urls')),
    path('sales/', include('sales.urls')),
    path('expenses/', include('expenses.urls')),
]
