from django.urls import path, include
from django.contrib import admin
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('stocks/', include('stocks.urls')),
    path('purchases/', include('purchase.urls')),
]
