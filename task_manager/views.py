from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin


def index(request):
    return render(request, 'index.html')


class LoginView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'


    success_message = 'Вы залогинены'

