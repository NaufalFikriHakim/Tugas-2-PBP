from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.models import Task
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
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
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

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
        title = request.POST.get('title')
        description = request.POST.get('description')
        list_todo = Task.objects.create(title=title, description=description,date=datetime.date.today(),is_finished=False, user=request.user)
        response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
        return response
    
    return render(request, "create-todo.html")

def update(request,pk):

    todo = get_object_or_404(Task, pk = pk)
    todo.is_finished = not todo.is_finished
    todo.save()

    return redirect('todolist:show_todolist')

def delete(request,pk):

    todo = get_object_or_404(Task, pk = pk)
    todo.delete()

    return redirect('todolist:show_todolist')