from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse


def index(request):
    return render(request, 'index.html')


class LoginView(LoginView):
    template_name = 'users/login.html'
