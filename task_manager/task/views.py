from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView
from task_manager.task.models import Task
from task_manager.task.forms import TaskForm
from task_manager.task.filter import TaskFilter
from django_filters.views import FilterView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class TaskList(LoginRequiredMixin, FilterView):
    template_name = 'task/tasklist.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter

    def get_queryset(self):
        return Task.objects.all()


class TaskCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task/task_create.html'
    form_class = TaskForm
    success_message = _('You are create new tasks')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tasks')


class TaskEdit(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task/task_edit.html'
    fields = ['name', 'description', 'status', 'executor', 'labels']
    success_message = _('You are update task')

    def get_success_url(self):
        return reverse('tasks')


class TaskDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task/task_delete.html'
    success_message = _('Task successfully deleted')

    def get_success_url(self):
        return reverse('tasks')

    def delete(self, request, *args, **kwargs):
        if self.get_object().author != request.user:
            messages.error(self.request, _(
                'Unable to delete task because this task created not you'))
            return redirect('tasks')
        messages.success(self.request, _('Task successfully deleted'))
        return super().delete(request, *args, **kwargs)
