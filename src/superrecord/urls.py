from django.urls import path, include
from django.contrib import admin
from helpers import graphs as graph_view
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
    path('graphs/roles/', graph_view.roles_graph, name='roles_data'),
    path('graphs/stocks/', graph_view.stocks_graph, name='stocks_data'),
    path('graphs/sales/', graph_view.sales_graph, name='sales_data'),
    path('graphs/expenses/', graph_view.expenses_graph, name='expenses_data')
]
