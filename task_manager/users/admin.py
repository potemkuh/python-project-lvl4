from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from task_manager.users.models import User

from django.views.generic.base import TemplateView
admin.site.register(User, UserAdmin)
