from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView
from task_manager.label.models import Label
from task_manager.label.forms import LabelsForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class LabelsList(LoginRequiredMixin, ListView):
    template_name = 'label/labels_list.html'
    context_object_name = 'labels'

    def get_queryset(self):
        return Label.objects.all()


class LabelsCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Label
    template_name = 'label/labels_create.html'
    form_class = LabelsForm
    success_message = _('You are create new label')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('labels')


class LabelsEdit(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Label
    template_name = 'label/labels_edit.html'
    form_class = LabelsForm
    success_message = _('You are update label')

    def get_success_url(self):
        return reverse('labels')


class LabelsDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'label/labels_delete.html'
    success_message = _('Label successfully deleted')

    def get_success_url(self):
        return reverse('labels')

    def delete(self, request, *args, **kwargs):
        if self.get_object().label.all().exists():
            messages.error(self.request, _('Unable to delete label because it is in use'))
            return redirect('labels')
        messages.success(self.request, _('Label successfully deleted'))
        return super().delete(request, *args, **kwargs)
