from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    def str(self):
        return self.get_full_name()

class Status(models.Model):
    name = models.CharField('name', max_length=64, unique=True)

    def str(self):
        return self.name
