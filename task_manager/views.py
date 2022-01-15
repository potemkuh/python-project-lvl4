from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.translation import gettext as _


class LoginView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'

    success_message = _('You are logged in')


class LogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)
