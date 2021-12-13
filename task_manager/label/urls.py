from django.urls import path
from task_manager.label import views


urlpatterns = [
    path('labels/', views.LabelsList.as_view(), name='labels'),
    path('labels/create/', views.LabelsCreate.as_view(), name='create_label'),
    path('labels/<int:pk>/update/', views.LabelsEdit.as_view(), name='label_edit'),
    path('labels/<int:pk>/delete/', views.LabelsDelete.as_view(), name='label_delete'),
]
