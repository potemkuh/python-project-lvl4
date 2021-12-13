from django.forms import ModelForm
from task_manager.task.views import Task



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields =['name', 'description', 'status', 'executor', 'labels']
