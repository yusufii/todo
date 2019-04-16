from .models import *
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .forms import TodoForm


def index(request):
    todo_list = TodoList.objects.all()
    context = {'todo_list' : todo_list}
    return render(request, 'todo/index.html', context)


def todo_detail(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})


def todo_new(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm()
    return render(request, 'todo/todo_edit.html', {'form': form})


def todo_edit(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_edit.html', {'form': form})


def todo_delete(request, pk):
    todo = TodoList.objects.get(pk=pk)
    todo.delete()
    return redirect("/")