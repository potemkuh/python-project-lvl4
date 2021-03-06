from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class CheckUserForDelMixin(UserPassesTestMixin):

    def test_func(self):
        user = self.get_object()
        return user == self.request.user

    def dispatch(self, request, *args, **kwargs):
        self.permission_denied_message = _('You do not have permission to delete another user.')
        self.permission_denied_url = reverse_lazy('users')
        return super().dispatch(request, *args, **kwargs)


class SuccessMessageDeleteMixin():
    success_message = ''

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, self.success_message)
        return response


class CheckUserForEditMixin(UserPassesTestMixin):

    def test_func(self):
        user = self.get_object()
        return user == self.request.user

    def dispatch(self, request, *args, **kwargs):
        self.permission_denied_message = _('You do not have permission to modify another user.')
        self.permission_denied_url = reverse_lazy('users')
        return super().dispatch(request, *args, **kwargs)
