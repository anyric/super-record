from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, UpdateView, DetailView, DeleteView, CreateView, TemplateView )
from bootstrap_modal_forms.generic import BSModalCreateView
from .forms import ( UserRegisterForm, EditProfileForm, 
    RoleCreationForm, EditRoleForm )
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import Group
from .models import User, Role
from .permissions import assign_permissions, remove_permissions

@method_decorator(login_required, name='dispatch')
class UserListView(ListView):
    queryset = User.objects.all().order_by('id')
    paginate_by = 7
    context_object_name = 'user_list'
    template_name = 'accounts/user.html'

@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView, DetailView):
    template_name = 'accounts/edit.html'
    pk_url_kwarg = 'id'
    form_class = EditProfileForm
    queryset = User.objects.all()
    success_url = reverse_lazy('setting')

@method_decorator(login_required, name='dispatch')
class PasswordUpdateView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    pk_url_kwarg = 'id'
    form_class = PasswordChangeForm
    queryset = User.objects.all()
    success_url = reverse_lazy('setting')

@method_decorator(login_required, name='dispatch')
class DeactivateView(DeleteView):
    template_name = 'accounts/deactivate.html'
    pk_url_kwarg = 'id'
    queryset = User.objects.all()
    success_url = reverse_lazy('setting')

@method_decorator(login_required, name='dispatch')
class ActivateView(DeleteView):
    template_name = 'accounts/activate.html'
    pk_url_kwarg = 'id'
    queryset = User.objects.all()
    success_url = reverse_lazy('setting')

@method_decorator(login_required, name='dispatch')
class SignUpView(BSModalCreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/signup.html'
    success_message = 'Success: Sign up succeeded.'
    success_url = reverse_lazy('setting')

@method_decorator(login_required, name='dispatch')
class RoleCreationView(CreateView):
    form_class = RoleCreationForm
    template_name = 'accounts/add_role.html'
    success_message = 'Success: Role creation succeeded.'
    success_url = reverse_lazy('setting')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            role = form.save()

            perm = [request.POST['user_perm']]
            if 'full' in perm:
                assign_permissions(role, perm, full=True)
            else:
                assign_permissions(role, perm)

            return HttpResponseRedirect(self.success_url)

        return render(request, self.success_url, {'form': form})

@method_decorator(login_required, name='dispatch')
class RoleListView(ListView):
    queryset = Role.objects.all().order_by('id')
    paginate_by = 7
    context_object_name = 'role_list'
    template_name = 'accounts/roles.html'

@method_decorator(login_required, name='dispatch')
class EditRoleView(UpdateView, DetailView):
    template_name = 'accounts/edit_role.html'
    pk_url_kwarg = 'id'
    form_class = EditRoleForm
    queryset = Role.objects.all()
    success_url = reverse_lazy('setting')
    old_perms = []

    def get(self, request, *args, **kwargs):
        self.id = kwargs['id']
        self.edit_role = Role.objects.get(id=self.id)

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['role_perms'] = self.edit_role.permissions.all().values_list('codename', flat=True)
    
        return context
      
    def post(self, request, *args, **kwargs):
        id = kwargs['id']
        edit_role = Role.objects.get(id=id)
        self.old_perms += edit_role.permissions.all().values_list('codename', flat=True)
        new_perm = request.POST.getlist('user_perm')

        if not new_perm:
            raise ValueError("You must assign atleast 1 permission for the new role")

        if 'full' in new_perm or len(new_perm) == 4:
            edit_role.permissions.remove()
            assign_permissions(edit_role, new_perm, full=True)
        else:
            perms = []
            if len(new_perm) > 1:
                for p in new_perm:
                    if p not in self.old_perms:
                        perms += p
                        assign_permissions(edit_role, perms)
                remove_permissions(edit_role, new_perm, self.old_perms)
            else:
                if new_perm not in self.role_perms:
                    assign_permissions(edit_role, new_perm)
                remove_permissions(edit_role, new_perm, self.old_perms)

        return super().post(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class DeleteRoleView(DeleteView):
    template_name = 'accounts/delete_role.html'
    pk_url_kwarg = 'id'
    queryset = Role.objects.all()
    success_url = reverse_lazy('setting')

@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = 'accounts/home.html'

@login_required
def product(request):
    return render(request, 'accounts/product.html', {})

@login_required
def purchase(request):
    return render(request, 'accounts/purchase.html', {})

@login_required
def setting(request):
    return render(request, 'accounts/setting.html', {})

@login_required
def sales(request):
    return render(request, 'accounts/sales.html', {})

@login_required
def expense(request):
    return render(request, 'accounts/expense.html', {})

