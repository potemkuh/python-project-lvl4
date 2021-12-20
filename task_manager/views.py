from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


class LoginView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'

    success_message = 'Вы залогинены'

class LogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Вы разлогинены')
        return super().dispatch(request, *args, **kwargs)
