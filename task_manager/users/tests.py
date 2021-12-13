from django.test import TestCase
from django.test.client import Client
from django.urls import reverse



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
