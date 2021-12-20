from django.urls import path
from task_manager.status import views


urlpatterns = [
    path('', views.StatusList.as_view(), name='statuses'),
    path('create/', views.StatusCreate.as_view(), name='create_status'),
    path('<int:pk>/update/', views.StatusEdit.as_view(), name='status_edit'),
    path('<int:pk>/delete/', views.StatusDelete.as_view(), name='status_delete'),
]
