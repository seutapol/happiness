from django.urls import path
from .views import login_view, logout_view, todos_list, todo_detail, create_todo, delete_todo

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('todos/', todos_list, name='todos_list'),
    path('todos/<int:id>', todo_detail, name='todo_detail'),
    path('todos/new/', create_todo, name='create_todo'),
    path('todos/<int;id>/delete/', delete_todo, name='delete_todo')
    
]
