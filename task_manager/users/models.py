from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
