from django.urls import path
from task_manager.task import views


urlpatterns = [
    path('', views.TaskList.as_view(), name='tasks'),
    path('create/', views.TaskCreate.as_view(), name='create_task'),
    path('<int:pk>/update/', views.TaskEdit.as_view(), name='task_edit'),
    path('<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),
]
