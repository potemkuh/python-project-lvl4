from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView
from task_manager.users.models import Status, Task
from django.forms import ModelForm



class UsersList(ListView):
    model = get_user_model()
    template_name = "users/users.html"
    context_object_name = "users"


class UserForm(UserCreationForm):
    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

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

class LoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('index')

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

class StatusList(LoginRequiredMixin, ListView):
    template_name = 'status/statuslist.html'
    context_object_name = 'statuses'
    
    def get_queryset(self):
        return Status.objects.all()

class StatusCreate(LoginRequiredMixin, CreateView):
    model = Status
    template_name = 'status/statuses_create.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('statuses')

class StatusEdit(LoginRequiredMixin, UpdateView):
    model = Status
    template_name = 'status/status_edit.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('statuses')

class StatusDelete(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'status/status_delete.html'

    def get_success_url(self):
        return reverse('statuses')

class TaskList(LoginRequiredMixin, ListView):
    template_name = 'task/tasklist.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return Task.objects.all()

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields =['name', 'description', 'status', 'executor']


class TaskCreate(SuccessMessageMixin, CreateView):
    model = Task
    template_name = 'task/task_create.html'
    form_class = TaskForm
    successmessage = 'Вы созадли новую задачу'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskEdit(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task/task_edit.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task/task_delete.html'

    def get_success_url(self):
        return reverse('tasks')

class LabelsList(LoginRequiredMixin, ListView):
    template_name = 'labels/labels_list.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return Task.objects.all()

class LabelsForm(ModelForm):
    class Meta:
        model = Task
        fields =['name']

class LabelsCreate(SuccessMessageMixin, CreateView):
    model = Task
    template_name = 'labels/labels_create.html'
    form_class = LabelsForm
    successmessage = 'Вы созадли новую метку'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class LabelsEdit(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'labels/labels_edit.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('tasks')

class LabelsDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'labels/labels_delete.html'

    def get_success_url(self):
        return reverse('tasks')