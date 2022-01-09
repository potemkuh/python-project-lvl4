from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import TextField
from django.utils.translation import gettext_lazy as _
from task_manager.status.models import Status
from task_manager.label.models import Label


class Task(models.Model):
    name = models.CharField(_('name'), max_length=64)
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT,
                                related_name='author',
                                verbose_name=_('author'))
    executor = models.ForeignKey(get_user_model(), on_delete=models.PROTECT,
                                related_name='executor',
                                verbose_name=_('executor'),
                                blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT,
                                related_name='status',
                                verbose_name=_('status'))
    description = TextField(_('description'), blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)
    labels = models.ManyToManyField(Label, related_name='labels',
                                    verbose_name=_('labels'),
                                    blank=True)

    def __str__(self):
        return self.name
