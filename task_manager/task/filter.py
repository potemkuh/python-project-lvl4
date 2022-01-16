from django_filters import FilterSet
from django_filters.filters import BooleanFilter, ModelChoiceFilter
from django import forms
from django.utils.translation import gettext_lazy as _
from task_manager.label.models import Label
from task_manager.task.models import Task


class TaskFilter(FilterSet):
    self_tasks = BooleanFilter(
        widget=forms.CheckboxInput,
        field_name=_('creator'),
        method='filter_self_tasks',
        label=_('Only their own tasks'),
    )

    label = ModelChoiceFilter(
        queryset=Label.objects.all(),
        field_name='labels',
        label=_('Label'),
    )

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'author', 'label', 'self_tasks']