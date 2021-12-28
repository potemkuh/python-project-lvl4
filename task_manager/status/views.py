from django.views.generic import CreateView, ListView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView
from task_manager.users.models import Status
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages



class StatusList(LoginRequiredMixin, ListView):
    template_name = 'status/statuslist.html'
    context_object_name = 'statuses'
    
    def get_queryset(self):
        return Status.objects.all()


class StatusCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Status
    template_name = 'status/statuses_create.html'
    fields = ['name']
    success_message = 'Статус успешно создан'

    def get_success_url(self):
        return reverse('statuses')


class StatusEdit(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Status
    template_name = 'status/status_edit.html'
    fields = ['name']
    success_message = 'Статус успешно изменён'

    def get_success_url(self):
        return reverse('statuses')


class StatusDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'status/status_delete.html'
    success_message = 'Статус успешно удалён'

    def get_success_url(self):
        return reverse('statuses')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, ('Статус успешно удалён'))
        return super().delete(request, *args, **kwargs)
