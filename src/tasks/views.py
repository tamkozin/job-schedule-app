from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def task_list(request):
    """
    ログイン中のユーザが登録したタスク一覧を表示するビュー。
    タスクはユーザが把握しやすいよう、締切期限順に並べて表示をする。
    """
    tasks = Task.objects.filter(user=request.user).order_by('deadline')
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    """
    ログイン中のユーザがタスクを登録するためのビュー。
    - POST: 入力内容を保持し、リダイレクト。
    - GET: 空のフォームを表示
    """
    form = TaskForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return redirect('task_list')
    
    return render(request, 'task_create.html', {'form': form})

def register(request):
    """
    新規ユーザ登録ページの処理。
    - POST: フォーム送信時にユーザ作成
    - GET: 空のフォームを表示
    """
    form = UserCreationForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('login')
    
    return render(request, 'register.html', {'form': form})

def task_delete(request, pk):
    """
    ユーザが登録したタスクを削除するビュー。
    - POST: タスクを削除し一覧ページにリダイレクト
    - GET: タスクを削除せず、一覧ページにリダイレクト
    """
    task = get_object_or_404(Task, pk=pk, user=request.user)
    
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    
    return redirect('task_list')

def index(request):
    """
    トップページを表示するビュー。
    """
    return render(request, 'index.html')