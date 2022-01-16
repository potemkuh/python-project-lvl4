from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView
from task_manager.users.forms import UserForm
from task_manager.users.mixins import SuccessMessageDeleteMixin, CheckUserForDelMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class UsersList(ListView):
    model = get_user_model()
    template_name = "users/users.html"
    context_object_name = "users"

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'password1',
                  'password2']


class CreateUser(SuccessMessageMixin, CreateView):
    model = get_user_model()
    template_name = 'users/create.html'
    form_class = UserForm
    success_message = _('User successfully registered')

    def get_success_url(self):
        return reverse('login')


class EditUser(LoginRequiredMixin, CheckUserForDelMixin,
               SuccessMessageMixin, UpdateView):
    model = get_user_model()
    template_name = 'users/edit_user.html'
    form_class = UserForm
    success_message = _('User successfully updated')
    permission_denied_url = reverse_lazy('users')
    permission_denied_message = _('You do not have permission to modify another user.')

    def get_success_url(self):
        return reverse('users')

    def handle_no_permission(self):
        messages.error(self.request, self.get_permission_denied_message())
        return redirect(self.permission_denied_url)


class DelUser(LoginRequiredMixin, CheckUserForDelMixin,
              SuccessMessageMixin, DeleteView):
    model = get_user_model()
    template_name = 'users/delete_user.html'
    success_message = _('User deleted')
    permission_denied_url = reverse_lazy('users')
    permission_denied_message = _('You do not have permission to modify another user.')

    def get_success_url(self):
        return reverse('users')

    def handle_no_permission(self):
        messages.error(self.request, self.get_permission_denied_message())
        return redirect(self.permission_denied_url)

    def delete(self, request, *args, **kwargs):
        if self.get_object().executor.all().exists() \
                or self.get_object().author.all().exists():
            messages.error(self.request, _(
                'Unable to delete user because it is in use'))
            return redirect('users')
        messages.success(self.request, _('User deleted'))
        return super().delete(request, *args, **kwargs)