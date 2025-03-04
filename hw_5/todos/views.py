from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm

def login_view(request):
    if request.method == "POST":
       form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('todos_list')
    else:
        form = AuthenticationForm()
    return render(request, 'todos/login.html', {'form': form})

def logout_view(request):
    logout(request):
        return redirect('login')
    
    
    
@login_required
def todos_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos/todos_list.html', {'todos': todos})

@login_required
def todo_detail(request, id):
    todo = Todo.objects.get(id=id, user=request.user)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

@login_required
def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todos_list')
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form})

@login_required
def delete_todo(request, id):
    todo = Todo.objects.get(id=id, user=request.user)
    if todo:
        todo.delete()
    return redirect('todos_list')

    

# Create your views here.
