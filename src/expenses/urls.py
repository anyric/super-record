from django.urls import path
from expenses import views as expenses_views

urlpatterns = [
    path('expenses/', expenses_views.ExpensesListView.as_view(), name='expenses'),
    # path('expense/', expenses_views.ExpensesCreationView.as_view(), name='expense'),
    # path('edit_expense/<int:id>/', expenses_views.EditExpensesView.as_view(), name='edit_expense'),
    # path('delete_expense/<int:id>/', expenses_views.DeleteExpensesView.as_view(), name='delete_expense')
]
