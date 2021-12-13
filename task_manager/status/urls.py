from django.urls import path
from task_manager.status import views


urlpatterns = [
    path('statuses/', views.StatusList.as_view(), name='statuses'),
    path('statuses/create/', views.StatusCreate.as_view(), name='create_status'),
    path('statuses/<int:pk>/update/', views.StatusEdit.as_view(), name='status_edit'),
    path('statuses/<int:pk>/delete/', views.StatusDelete.as_view(), name='status_delete'),
]
