from django.urls import path
from stocks import views as product_view

urlpatterns = [
    path('products/', product_view.ProductListView.as_view(), name='products'),
    path('product/', product_view.ProductCreationView.as_view(), name='product'),
    path('edit_product/<int:id>/', product_view.EditProductView.as_view(), name='edit_product'),
    path('delete_product/<int:id>/', product_view.DeleteProductView.as_view(), name='delete_product'),
    path('product_report/', product_view.ProductPDFView.as_view(), name='product_report')
]