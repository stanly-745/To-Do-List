from django.shortcuts import render,redirect
from .models import *
from .form import *
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login,authenticate
from django.contrib import messages

# Create your views here.

#Login page
class loginview(LoginView):
    template_name='App/login.html'
    fields='__all__'
    redirect_authendicated_user=True
    def get_success_url(self):
        return reverse_lazy('task')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('task')
    else:
        form=CreateUserForm()
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Account was created for')
                return redirect('login')

        context={'form':form}
        return render(request,'App/register.html',context)

    

#Task list
@login_required(login_url='login')
def TaskList(request):
    if 'q' in request.GET:
        q=request.GET['q']
        object_list=Task.objects.filter(title__icontains=q)
    else:
        object_list=Task.objects.filter(user=request.user)
    data=Task.objects.filter(user=request.user)
    count=data.filter(Complete=False).count()
    context={
        'task':object_list,
        'count':count
    }
    
    return render(request,'App/Task_list.html',context)

#Task detail
@login_required(login_url='login')
def TaskDetail(request,pk):
    objects=Task.objects.get(id=pk)
    Context={
        'task':objects
    }
    return render(request,'App/Task.html',Context)

#Create Task
@login_required(login_url='login')
def createtask(request):
    
    forms=TaskForm
    if request.method=='POST':
        forms=TaskForm(request.POST)
        if forms.is_valid():
            obj=forms.save(commit=False)
            obj.user=request.user
            obj.save()
        return redirect('/')
    Context={
        'form':forms
    }
    return render(request,'App/task_form.html',Context)

#Edit Task
@login_required(login_url='login')
def Update(request,pk):
    task=Task.objects.get(id=pk)
    forms=TaskForm(instance=task)
    if request.method=='POST':
        forms=TaskForm(request.POST,instance=task)
        if forms.is_valid():
            forms.save()
            return redirect('/')

    Context={
        'form':forms
    }
    return render(request,'App/task_form.html',Context)

#Delete Task
@login_required(login_url='login')
def Delete(request,pk):
    task=Task.objects.get(id=pk)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    Context={'item':task}
    return render(request,'App/delete.html',Context)