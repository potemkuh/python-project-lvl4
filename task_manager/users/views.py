from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView
from task_manager.users.forms import UserForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


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
    success_message = 'Пользователь успешно зарегистрирован'

    def get_success_url(self):
        return reverse('login')


class EditUser(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'users/edit_user.html'
    form_class = UserForm
    success_message = 'Пользователь успешно изменён'

    def get_success_url(self):
        return reverse('users')

class SuccessMessageDeleteMixin():
    success_message = ''

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, self.success_message)
        return response

class DelUser(SuccessMessageDeleteMixin, LoginRequiredMixin, DeleteView):
    model = get_user_model()
    template_name = 'users/delete_user.html'
    success_message = 'Пользователь успешно удален'

    
    def get_success_url(self):
        return reverse('users')
