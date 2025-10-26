from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import TaskForm
from .models import Task

def task_list(request):
    tasks = Task.objects.fileter(user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_create.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def task_list(request):
    return render(request, 'task_list.html')