from django.views.generic import CreateView, ListView
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView
from task_manager.status.models import Status
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from task_manager.status.forms import StatusForm
from django.utils.translation import gettext_lazy as _


class StatusList(LoginRequiredMixin, ListView):
    template_name = 'status/statuslist.html'
    context_object_name = 'statuses'

    def get_queryset(self):
        return Status.objects.all()


class StatusCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Status
    template_name = 'status/statuses_create.html'
    form_class = StatusForm
    success_message = _('You are create new status')

    def get_success_url(self):
        return reverse('statuses')


class StatusEdit(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Status
    template_name = 'status/status_edit.html'
    form_class = StatusForm
    success_message = _('You are update status')

    def get_success_url(self):
        return reverse('statuses')


class StatusDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'status/status_delete.html'
    success_message = _('Status successfully deleted')

    def get_success_url(self):
        return reverse('statuses')

    def delete(self, request, *args, **kwargs):
        if self.get_object().labels.all().exists():
            messages.error(self.request, _('Unable to delete status because it is in use'))
            return redirect('statuses')
        messages.success(self.request, _('Status successfully deleted'))
        return super().delete(request, *args, **kwargs)
