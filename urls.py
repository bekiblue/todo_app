# todo_project/urls.py
from django.urls import path
from todo_app.views import task_list, task_detail

urlpatterns = [
    path('tasks/', task_list),
    path('tasks/<int:pk>/', task_detail),
]

