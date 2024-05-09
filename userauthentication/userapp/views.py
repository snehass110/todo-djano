from django.shortcuts import render,redirect
from .models import *
from userauthentication.settings import EMAIL_HOST_USER
from django.contrib import  messages
from django.core.mail import send_mail
from  django.conf import settings
from  django.contrib.auth import authenticate
import uuid
from  django.contrib.auth.models import User
from django.http import  HttpResponse
from .forms  import *
def regis(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        pas=request.POST.get('password')


        if User.objects.filter(email=email).first():
            messages.success(request,"email already taken")
            return redirect(regis)
        if User.objects.filter(username=uname).first():
            messages.success(request,"username already taken")
            return redirect(regis)

        user_obj=User(username=uname,email=email)
        user_obj.set_password(pas)
        user_obj.save()
        auth_token=str(uuid.uuid4())
        profile_obj=profile1.objects.create(user=user_obj,auth_token=auth_token)
        profile_obj.save()
        send_mail_regis(email,auth_token)
        return redirect(success)
    return render(request,"register.html")

def send_mail_regis(email,token):
    subject="your account has been verified"
    message=f"pass the link to verify your account http:127.0.0.1:8000/verify/{token}"
    email_from=EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_from,recipient)

def success(request):
    return render(request,"success.html")

def login(request):
    global User;
    if request.method=='POST':
        username=request.POST.get('uname')
        pas=request.POST.get('password')
        user_obj=User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request,'user not found')
            return  redirect(login)
        profile_obj=profile1.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request,'profile verified cheek your email')
            return  redirect(login)
        User=authenticate(username=username,password=pas)

        if User is None:
            messages.success(request,'wrong password or username')
            return  redirect(login)

        data = Todo.objects.all()
        completed_tasks_count = 0
        pending_tasks_count = 0

        for todo in data:
            if todo.status == 'completed':
                completed_tasks_count += 1
            elif todo.status == 'pending' or todo.status == 'in-progress':
                pending_tasks_count += 1
        unique_project_titles = set(i.project_title for i in data)
        return render(request, 'home.html', {'unique_project_titles': unique_project_titles
                                             ,
        'completed_tasks_count': completed_tasks_count,
        'pending_tasks_count': pending_tasks_count,'data': data})


        # for i in data:
        #     a = i.project_title1
        #     pt.append(a)
        # s = zip(pt)
        # return  render(request,'home.html',{'s':s})
    return render(request,'login.html')

def verify(request,auth_token):
    profile_obj=profile1.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request,'your account already verified')
            redirect(login)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'ur account verified')
        return redirect(login)
    else:
        return redirect(error)

def error(request):
    return  render(request,'error.html')

#
#
# def create_success(request,id):
#     projects = Project.objects.get(id=id)
#     return render(request, 'create.html', {'projects': projects})
from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from .forms import project_form
from .models import project_model

def create(request):
    if request.method == "POST":
        form = project_form(request.POST)
        if form.is_valid():
            project_title = form.cleaned_data['project_title']
            project = project_model(project_title=project_title)
            project.save()

            return render(request, 'create.html', {'project_title': project_title})
        else:
            return HttpResponse("Enter valid data")

    return render(request, 'home.html')

from django.shortcuts import render, redirect
from .forms import TodoForm

# def create_todo(request):
#     if request.method == 'POST':
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("suess")
#     return render(request, 'create.html', )

def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            project_title = form.cleaned_data['project_title']
            todo_name = form.cleaned_data['todo_name']
            todo_description = form.cleaned_data['todo_description']
            created_time = form.cleaned_data['created_time']
            status = form.cleaned_data['status']
            project = Todo.objects.create(project_title=project_title, todo_name=todo_name,
                                          todo_description=todo_description, created_time=created_time, status=status)

            project.save()

            return render(request, 'create.html', {'project_title': project_title})
        else:
            return HttpResponse("Enter valid data")

    return render(request, 'create.html')
from django.shortcuts import render, HttpResponse
from .forms import TodoForm
from .models import Todo

#
# def feedback(request):
#     data=Todo.objects.all()
#     pt=[]
#
#     for i in data:
#         a=i.project_name
#         pt.append(a)
#
#     s=zip(pt)
#
#     return render(request, '3.html', {'s':s})
# ml')
# def create(request):
# def view_project(request, project_title):

#     # a=Todo.objects.get(project_title=project_title)
#     a = Todo.objects.filter(project_title=project_title)
#     pt=[]
#     tt=[]
#     td=[]
#     ct=[]
#     s=[]
#     for i in a:
#         b = i.project_title
#         pt.append(b)
#         c= i.todo_name
#         tt.append(c)
#         d= i.todo_description
#         td.append(d)
#         e= i.created_time
#         ct.append(e)
#         f= i.status
#         s.append(f)
#
#
#
#     k = zip(pt,tt,td,ct,s)
#
#     return render(request, 'view.html',{'k':k})
# def view_project(request, project_title):
#     todos = Todo.objects.filter(project_title=project_title)
#


def view_project(request, project_title):
    todos = Todo.objects.filter(project_title=project_title)
    pt = []
    tt=[]
    td=[]
    ct=[]
    s=[]
    for i in todos:
        b = i.project_title
        pt.append(b)
        c= i.todo_name
        tt.append(c)
        d= i.todo_description
        td.append(d)
        e= i.created_time
        ct.append(e)
        f= i.status
        s.append(f)


    completed_tasks_count = 0
    pending_tasks_count = 0

    for todo in todos:
        if todo.status == 'completed':
            completed_tasks_count += 1
        elif todo.status == 'pending' or todo.status == 'in-progress':
            pending_tasks_count += 1

    return render(request, 'view.html', {
        'project_title': project_title,
        'completed_tasks_count': completed_tasks_count,
        'pending_tasks_count': pending_tasks_count,
        'todos': todos
    })
def view_projectdetail(request, project_title):
    todos = Todo.objects.filter(project_title=project_title)


    return render(request, 'view2.html', {
                                          'project_title': project_title,
                                          'todos': todos
                                          })
# def edit(request,todo_name):
#     todos = Todo.objects.filter(todo_name=todo_name)
#
#     if request.method == 'POST':
#         todos.todo_name = request.POST.get('todo_name')
#         todos.todo_description = request.POST.get('todo_description')
#         todos.created_time = request.POST.get('created_time')
#         todos.status = request.POST.get('status')
#         todos.save()
#         return render(request, 'view2.html')
#     return render(request,'edit.html',{'todos':todos})
from django.shortcuts import render, redirect
from .models import Todo

def edit(request, todo_name):

    todo = Todo.objects.filter(todo_name=todo_name).first()

    if request.method == 'POST':

        todo.todo_name = request.POST.get('todo_name', '')
        todo.todo_description = request.POST.get('todo_description', '')
        todo.created_time = request.POST.get('created_time', '')
        todo.status = request.POST.get('status', '')
        todo.save()

        return render(request,'view2.html')


    return render(request, 'edit.html', {'todo': todo})
def delete(request,todo_name):
    todos = Todo.objects.filter(todo_name=todo_name)

    todos.delete()
    return render(request, 'view2.html')
    # return redirect(update)