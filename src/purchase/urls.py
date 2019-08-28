from django.urls import path
from purchase import views as purchase_views

urlpatterns = [
    path('purchase/', purchase_views.Purchase.as_view(), name='purchase'),
]
