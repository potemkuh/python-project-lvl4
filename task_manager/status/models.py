from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    name = models.CharField(_('name'), max_length=64, unique=True)
    create_date = models.DateTimeField(_('create_date'), auto_now_add=True)

    def __str__(self):
        return self.name
