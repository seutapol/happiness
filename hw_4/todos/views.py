from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList, Todo

def redirect_to_todo_lists(request):
    return redirect('todo_lists')

def todo_list_view(request):
    todo_lists = TodoList.objects.all()
    return render(request, 'todos/todo_list.html', {'todo_lists': todo_lists})

def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todos = Todo.objects.filter(todo_list=todo_list)
    return render(request, 'todos/todo_list_detail.html', {'todo_list': todo_list, 'todos': todos})

def delete_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todo_list.delete()
    return redirect('todo_lists')

def edit_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == 'POST':
        todo_list.title = request.POST['title']
        todo_list.description = request.POST['description']
        todo_list.save()
        return redirect('todo_lists')
    return render(request, 'todos/edit_todo_list.html', {'todo_list': todo_list})

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo_list_id = todo.todo_list.id
    todo.delete()
    return redirect('todo_list_detail', id=todo_list_id)

def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.description = request.POST['description']
        todo.due_date = request.POST['due_date']
        todo.status = 'status' in request.POST
        todo.save()
        return redirect('todo_list_detail', id=todo.todo_list.id)
    return render(request, 'todos/edit_todo.html', {'todo': todo})