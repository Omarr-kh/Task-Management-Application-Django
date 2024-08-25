from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-task/', views.add_task, name='add-task'),
    path('view-task/<int:task_id>/', views.view_task, name='view-task'),
    path('delete-task/<int:task_id>/',
         views.delete_task, name='delete-task'),
    path('update-task/<int:task_id>/', views.update_task, name='update-task')
]
