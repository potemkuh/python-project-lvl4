from django.urls import path
from django.views.generic.base import TemplateView
from task_manager.users import views


urlpatterns = [
    path('create/', views.CreateUser.as_view(), name='create'),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('users/<int:pk>/update/', views.EditUser.as_view(), name='edit_user'),
    path('users/<int:pk>/delete/', views.DelUser.as_view(), name='delete_user'),
]
