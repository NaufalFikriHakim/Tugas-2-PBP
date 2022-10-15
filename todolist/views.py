from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.models import Task
from django.core import serializers
import datetime
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from todolist.forms import TaskForm
# Create your views here.



def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data = Task.objects.all()
    context = {
        'list_todo': data,
        'nama': 'Naufal Fikri Hakim',
        'npm': '2106750566',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login/')
def show_create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        form.instance.user = request.user
        form.instance.date = datetime.datetime.now()

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("todolist:show_todolist"))

    else:
        form = TaskForm()

        return render(request, 'create-todo.html', {'form':form})

def update(request,pk):

    task = Task.objects.filter(id=pk).first()
    task.is_finished = task.is_finished ^ True
    task.save()
    return HttpResponse(b"CHANGED", status=201) # used for asynchronus task status change
def delete(request,pk):

    Task.objects.filter(id=pk).first().delete()
    return HttpResponse(b"DELETED", status=201) # used for asynchronus delete

@login_required(login_url='/todolist/login/')
def show_json(request):
    user = request.user
    data = Task.objects.filter(user=user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/todolist/login/')
def add_task(request):                      # asynchronus create task
    if request.method == 'POST':
        form = TaskForm(request.POST)

        form.instance.user = request.user
        form.instance.date = datetime.datetime.now()

        if form.is_valid():
            form.save()
            return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()