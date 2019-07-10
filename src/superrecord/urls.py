from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import index
from accounts import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/home/', user_views.home, name='home'),
    path('accounts/signup/', user_views.register, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('accounts/product/', user_views.product, name='product'),
    path('accounts/purchase/', user_views.purchase, name='purchase'),
]
