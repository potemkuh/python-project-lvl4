from django.urls import path
from django.views.generic.base import TemplateView
from task_manager.users import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    #path('', views.list_of_users),
    path('users/', views.UsersList.as_view(), name='users'),
    path('create/', views.CreateUser.as_view(), name='create'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('users/<int:pk>/update/', views.EditUser.as_view(), name='edit_user' ),
    path('users/<int:pk>/delete/', views.DelUser.as_view(), name='delete_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('statuses/', views.StatusList.as_view(), name='statuses'),
    path('statuses/create/', views.StatusCreate.as_view(), name='create_status'),
    path('statuses/<int:pk>/update/', views.StatusEdit.as_view(), name='status_edit'),
    path('statuses/<int:pk>/delete/', views.StatusDelete.as_view(), name='status_delete'),
    path('tasks/', views.TaskList.as_view(), name='tasks'),
    path('tasks/create/', views.TaskCreate.as_view(), name='create_task'),
    path('tasks/<int:pk>/update/', views.TaskEdit.as_view(), name='task_edit'),
    path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),
    path('labels/', views.LabelsList.as_view(), name='labels'),
    path('labels/create/', views.LabelsCreate.as_view(), name='create_label'),
    path('labels/<int:pk>/update/', views.LabelsEdit.as_view(), name='label_edit'),
    path('labels/<int:pk>/delete/', views.LabelsDelete.as_view(), name='label_delete'),
]
