from django.urls import path
from task_manager.label import views


urlpatterns = [
    path('', views.LabelsList.as_view(), name='labels'),
    path('create/', views.LabelsCreate.as_view(), name='create_label'),
    path('<int:pk>/update/', views.LabelsEdit.as_view(), name='label_edit'),
    path('<int:pk>/delete/', views.LabelsDelete.as_view(), name='label_delete'),
]
