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
]
