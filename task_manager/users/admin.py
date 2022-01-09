from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from task_manager.users.models import User
from task_manager.status.models import Status
from task_manager.task.models import Task
from task_manager.label.models import Label


admin.site.register([User, Status, Task, Label])
