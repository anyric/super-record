from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import index
from accounts import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/user/', user_views.UserListView.as_view(), name='user'),
    path('accounts/roles/', user_views.RoleListView.as_view(), name='roles'),
    path('accounts/role/', user_views.RoleCreationView.as_view(), name='role'),
    path('accounts/edit_role/<int:id>/', user_views.EditRoleView.as_view(), name='edit_role'),
    path('accounts/delete_role/<int:id>/', user_views.DeleteRoleView.as_view(), name='delete_role'),
    path('accounts/home/', user_views.Home.as_view(), name='home'),
    path('accounts/signup/', user_views.SignUpView.as_view(), name='signup'),
    path('accounts/edit/<int:id>/', user_views.EditProfileView.as_view(), name='edit'),
    path('accounts/change_password/', user_views.PasswordUpdateView.as_view(), name='change_password'),
    path('accounts/deactivate/<int:id>/', user_views.DeactivateView.as_view(), name='deactivate'),
    path('accounts/activate/<int:id>/', user_views.ActivateView.as_view(), name='activate'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('accounts/product/', user_views.Product.as_view(), name='product'),
    path('accounts/purchase/', user_views.Purchase.as_view(), name='purchase'),
    path('accounts/sales/', user_views.Sales.as_view(), name='sales'),
    path('accounts/expense/', user_views.Expense.as_view(), name='expense'),
    path('accounts/setting/', user_views.Setting.as_view(), name='setting'),
]
