from django.urls import path
from task_manager.users import views

urlpatterns = [
    path('', views.list_of_users),
    path('create/', views.create),
]