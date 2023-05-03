from django.urls import path

from . import views

app_name = 'front'
urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('task/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/toggle-status-api/', views.TaskToggleStatusAPI.as_view(), name='task_toggle_status_api'),
]
