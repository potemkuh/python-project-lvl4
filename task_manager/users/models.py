from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models.fields import TextField


class User(AbstractUser):
    
    def str(self):
        return self.get_full_name()

class Status(models.Model):
    name = models.CharField('name', max_length=64, unique=True)

    def str(self):
        return self.name

class Label(models.Model):
    name = models.CharField('name', max_length=64, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField('name', max_length=64)
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='author')
    executor = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='executor')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='status')
    description = TextField('description', blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)
    labels = models.ManyToManyField(Label, related_name='labels', blank=True)
