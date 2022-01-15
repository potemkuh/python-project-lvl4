from django.forms import ModelForm
from task_manager.status.views import Status


class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['name']
