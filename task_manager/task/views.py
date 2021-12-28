from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView
from task_manager.users.models import Label, Task
from task_manager.task.forms import TaskForm
from django_filters.views import FilterView
from django_filters import FilterSet
from django_filters.filters import BooleanFilter, ModelChoiceFilter
from django import forms
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class TaskFilter(FilterSet):
    self_tasks = BooleanFilter(
        widget = forms.CheckboxInput,
        field_name = _('creator'),
        method = 'filter_self_tasks',
        label = 'Only their own tasks',
    )

    label = ModelChoiceFilter(
        queryset = Label.objects.all(),
        field_name = _('labels'),
        label = 'Label',
    )

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'author', 'label', 'self_tasks']



class TaskList(LoginRequiredMixin, FilterView):
    template_name = 'task/tasklist.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter

    
    def get_queryset(self):
        return Task.objects.all()


class TaskCreate(SuccessMessageMixin, CreateView):
    model = Task
    template_name = 'task/task_create.html'
    form_class = TaskForm
    successmessage = _('You are create new tasks')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tasks')

class TaskEdit(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task/task_edit.html'
    fields = ['name', 'description', 'status', 'executor', 'labels']
    successmessage = _('You are update task')

    def get_success_url(self):
        return reverse('tasks')

class TaskDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task/task_delete.html'
    successmessage = _('Task successfully deleted')

    def get_success_url(self):
        return reverse('tasks')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Task successfully deleted'))
        return super().delete(request, *args, **kwargs)
