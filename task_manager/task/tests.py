from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from task_manager.users.models import Label, User, Task, Status


DATA_STATUS = {'name': 'new_status'}
DATA_LABLE = {'name': 'new_label'}
USER_NAME ='testuser'
USER_PASS ='12345'


def database_fill():
    Status.objects.create(name=DATA_STATUS['name'])
    Label.objects.create(name=DATA_LABLE['name'])
    User.objects.create_user(username=USER_NAME, password=USER_PASS)
    status = Status.objects.get(name=DATA_STATUS['name'])
    label = Label.objects.get(name=DATA_LABLE['name'])
    user = User.objects.get(username=USER_NAME)
    return status, label, user


def task_create_and_get_name():
    Task.objects.create(name = 'test_task',
                        description = 'description',
                        status = Status.objects.get(name=DATA_STATUS['name']),
                        author = User.objects.get(username=USER_NAME),
                        executor = User.objects.get(username=USER_NAME)
                        )
    return Task.objects.get(name='test_task')

def create_task_data(status, label, user):
    task_data = {
        'name': 'task_1',
        'description': 'description',
        'status': status.pk,
        'executor': user.pk,
        'author': user.pk,
        'labels': [label.pk],
    }
    return task_data

class TestLabels(TestCase):

    def test_create_task(self):
        client = Client()
        status, label, user = database_fill()
        task_data = create_task_data(status, label, user)
        client.force_login(user)
        # отправляем запрос на создание задачи
        response = client.post(reverse('create_label'), task_data, follow=True)
        # получаем название задачи
        db_task = Label.objects.get(name=task_data['name'])
        # проверка кода ответа
        self.assertEqual(response.status_code, 200)
        # проверили что задача есть в бд
        self.assertEqual(task_data['name'], db_task.name)


    def test_update_task(self):
        client = Client()
        status, label, user = database_fill()
        client.force_login(user)
        task = task_create_and_get_name()
        task_update = create_task_data(status, label, user)
        task_url = reverse('task_edit', args=[str(task.pk)])
        response = client.post(task_url, task_update, follow=True)
        db_task = Task.objects.get(pk=task.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(task_update['name'], db_task.name)

    def test_delete_task(self):
        client = Client()
        status, label, user = database_fill()
        client.force_login(user)
        task = task_create_and_get_name()
        task_delete_url = reverse('task_delete', args=[str(task.pk)])
        response = client.post(task_delete_url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Task.objects.all()), 0)