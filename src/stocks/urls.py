from django.urls import path
from stocks import views as product_view

urlpatterns = [
    path('products/', product_view.Product.as_view(), name='products'),
]