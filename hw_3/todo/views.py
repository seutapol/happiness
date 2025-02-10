from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Todo
from .forms import TodoForm

def get_todos(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todos_list.html', {'todos': todos})

def get_todo_by_id(request, todo_id):
    todo = Todo.objects.filter(id=todo_id).values().first()
    return JsonResponse(todo, safe=False) if todo else JsonResponse({'error': 'Todo not found'}, status=404)

def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todos/')
    else:
        form = TodoForm()
    return render(request, 'todo/create_todo.html', {'form': form})
    
    
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id) 
    todo.delete()
    return redirect('/todos/')   

# Create your views here.
