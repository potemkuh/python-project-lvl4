from django.forms import ModelForm
from task_manager.label.views import Label


class LabelsForm(ModelForm):
    class Meta:
        model = Label
        fields = ['name']
