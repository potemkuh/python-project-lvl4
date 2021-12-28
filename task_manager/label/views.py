from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView
from task_manager.users.models import Label
from task_manager.label.forms import LabelsForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class LabelsList(LoginRequiredMixin, ListView):
    template_name = 'label/labels_list.html'
    context_object_name = 'labels'
    
    def get_queryset(self):
        return Label.objects.all()

class LabelsCreate(SuccessMessageMixin, CreateView):
    model = Label
    template_name = 'label/labels_create.html'
    form_class = LabelsForm
    successmessage = 'Метка успешно создана'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('labels')


class LabelsEdit(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Label
    template_name = 'label/labels_edit.html'
    fields = ['name']
    successmessage = 'Метка успешно изменена'

    def get_success_url(self):
        return reverse('labels')


class LabelsDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'label/labels_delete.html'
    successmessage = 'Метка успешно удалена'

    def get_success_url(self):
        return reverse('labels')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, ('Метка успешно удалена'))
        return super().delete(request, *args, **kwargs)
