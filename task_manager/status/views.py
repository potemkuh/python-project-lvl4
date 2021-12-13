from django.views.generic import CreateView, ListView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView
from task_manager.users.models import Status


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
