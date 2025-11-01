from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required(login_url='login')
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('deadline')
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required(login_url='login')
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

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return redirect('task_list')

def index(request):
    return render(request, 'index.html')