from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from task_manager.users.models import Status, User


DATA = {'name': 'new'}
USER_NAME ='testuser'
USER_PASS ='12345'

class TestStatus(TestCase):

    def test_create_status(self):
        client = Client()
        user = User.objects.create_user(username=USER_NAME, password=USER_PASS)
        client.force_login(user)
        # отправляем запрос на создание статуса DATA
        response = client.post(reverse('create_status'), DATA)
        # получаем имя статуса
        db_stasus = Status.objects.get(name=DATA['name'])
        # проверили что был выполнен ридерект
        self.assertEqual(response.status_code, 302)
        # проверили что статус есть в бд
        self.assertEqual(DATA['name'], db_stasus.name)


    def test_delete_status(self):
        client = Client()
        user = User.objects.create_user(username=USER_NAME, password=USER_PASS)
        client.force_login(user)
        Status.objects.create(name='name')
        old_status = Status.objects.get(name='name')
        # получем урл с номером пкстатуса
        status_delete_url = reverse('status_delete', args=[str(old_status.pk)])
        # удаляем статус 
        response = client.post(status_delete_url)
        # проверили что был выполнен ридерект
        self.assertEqual(response.status_code, 302)
        # проверили размер дб
        self.assertEqual(len(Status.objects.all()), 0)

    def test_update_status(self):
        client = Client()
        user = User.objects.create_user(username=USER_NAME, password=USER_PASS)
        client.force_login(user)
        # создаем и получаем имя статуса
        Status.objects.create(name='name')
        name_status = Status.objects.get(name='name')
        # получем урл статуса
        status_url = reverse('status_edit', args=[str(name_status.pk)])
        # изменяем статус
        response = client.post(status_url, DATA)
        # получаем пк нового статуса
        db_status = Status.objects.get(pk=name_status.pk)
        # проверили что был выполнен ридерект
        self.assertEqual(response.status_code, 302)
        # проверяем присутсвие нового имени в бд
        self.assertEqual(DATA['name'], db_status.name)
