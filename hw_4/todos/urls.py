from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_todo_lists, name='home'),
    path('todo-lists/', views.todo_list_view, name='todo_lists'),
    path('todo-lists/<int:id>/', views.todo_list_detail, name='todo_list_detail'),
    path('todo-lists/<int:id>/delete/', views.delete_todo_list, name='delete_todo_list'),
    path('todo-lists/<int:id>/edit/', views.edit_todo_list, name='edit_todo_list'),
    path('todos/<int:id>/delete/', views.delete_todo, name='delete_todo'),
    path('todos/<int:id>/edit/', views.edit_todo, name='edit_todo'),
]