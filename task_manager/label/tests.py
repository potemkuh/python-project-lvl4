from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from task_manager.users.models import User
from task_manager.label.models import Label


DATA = {'name': 'new_label'}
USER_NAME = ' testuser'
USER_PASS = '12345'


class TestLabels(TestCase):

    def test_create_label(self):
        client = Client()
        user = User.objects.create_user(username=USER_NAME, password=USER_PASS)
        client.force_login(user)
        # отправляем запрос на создание метки DATA
        response = client.post(reverse('create_label'), DATA, follow=True)
        # получаем имя статуса
        db_lable = Label.objects.get(name=DATA['name'])
        # проверка ответа сервера
        self.assertEqual(response.status_code, 200)
        # проверили что статус есть в бд
        self.assertEqual(DATA['name'], db_lable.name)

    def test_delete_label(self):
        client = Client()
        user = User.objects.create_user(username=USER_NAME, password=USER_PASS)
        client.force_login(user)
        Label.objects.create(name='name')
        old_status = Label.objects.get(name='name')
        # получем урл с номером пк статуса
        lable_delete_url = reverse('label_delete', args=[str(old_status.pk)])
        # удаляем статус
        response = client.post(lable_delete_url, follow=True)
        # проверка ответа сервера
        self.assertEqual(response.status_code, 200)
        # проверили размер дб
        self.assertEqual(len(Label.objects.all()), 0)

    def test_update_label(self):
        client = Client()
        user = User.objects.create_user(username=USER_NAME, password=USER_PASS)
        client.force_login(user)
        # создаем и получаем имя статуса
        Label.objects.create(name='name')
        name_status = Label.objects.get(name='name')
        # получем урл статуса
        status_url = reverse('label_edit', args=[str(name_status.pk)])
        # изменяем статус
        response = client.post(status_url, DATA, follow=True)
        # получаем пк нового статуса
        db_lable = Label.objects.get(pk=name_status.pk)
        # проверка ответа сервера
        self.assertEqual(response.status_code, 200)
        # проверяем присутсвие нового имени в бд
        self.assertEqual(DATA['name'], db_lable.name)
