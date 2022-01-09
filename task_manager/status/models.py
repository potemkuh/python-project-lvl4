from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    name = models.CharField(_('name'), max_length=64, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
from task_manager.users.models import User
from task_manager.label.models import Label
from task_manager.task.models import Task
from task_manager.status.models import Status
