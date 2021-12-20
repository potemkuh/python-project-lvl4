from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView
from task_manager.users.forms import UserForm


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
    successmessage = 'User successfully registered'

    def get_success_url(self):
        return reverse('login')


class EditUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'users/edit_user.html'
    form_class = UserForm

    def get_success_url(self):
        return reverse('users')


class DelUser(LoginRequiredMixin, DeleteView):
    model = get_user_model()
    template_name = 'users/delete_user.html'
    
    def get_success_url(self):
        return reverse('users')
