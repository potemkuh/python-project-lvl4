from django.forms import ModelForm
from task_manager.task.views import Task
from django.utils.translation import gettext_lazy as _



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields =['name', 'description', 'status', 'executor', 'labels']
