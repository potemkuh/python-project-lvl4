from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from task_manager.users.models import User


USER_NAME = 'testuser'
USER_PASS = '12345'


class TestRegistrAndLogin(TestCase):
    def test_register(self):
        client = Client()
        username = 'test_user'
        password1 = '123Rjhjdfve'
        password2 = '123Rjhjdfve'
        user = {
            'first_name': 'test_first',
            'last_name': 'test_last',
            'username': username,
            'password1': password1,
            'password2': password2 
        }        
        reg = client.post(reverse('create'), user, follow=True)

        self.assertEqual(reg.status_code, 200)

    def test_login(self):
        client = Client()
        User.objects.create_user(username=USER_NAME, password=USER_PASS)
        user = {
            'username': USER_NAME,
            'password': USER_PASS             
        }
        res = client.post(reverse('login'), user, follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['user'].is_authenticated, True)
