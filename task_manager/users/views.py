from django.http import request
from django.shortcuts import render
from task_manager.users.models import Users


def list_of_users(request):
    data = Users.objects.all()
    return render(request, 'users.html', {'data': data})
