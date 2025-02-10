from django.urls import path
from .views import get_todos, get_todo_by_id, create_todo, delete_todo

urlpatterns = [
    path('todos/', get_todos,  name='get_todos'),
    path('todos/<int:todo_id>/', get_todo_by_id, name='get_todo_by_id'),
    path('todos/create/', create_todo, name='create_todo'),
    path('todos/<int:todo_id>/delete/', delete_todo, name='delete_todo'),
]