from django.urls import path
from django.contrib import admin
from .views import index
from accounts.views import login_view, register_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('accounts/login/', login_view),
    path('accounts/signup/', register_view),
    path('accounts/logout/', logout_view)
]
