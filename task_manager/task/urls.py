from django.urls import path
from task_manager.task import views


urlpatterns = [
    path('tasks/', views.TaskList.as_view(), name='tasks'),
    path('tasks/create/', views.TaskCreate.as_view(), name='create_task'),
    path('tasks/<int:pk>/update/', views.TaskEdit.as_view(), name='task_edit'),
    path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),
]
