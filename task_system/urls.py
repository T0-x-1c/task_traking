from django.urls import path 
from task_system import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('task-create/', views.TaskCreateView.as_view(), name='task_create'),
    path('task-update/<int:pk>', views.TaskUpdateView.as_view(), name='task_update'),
]