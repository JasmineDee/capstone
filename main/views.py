from django.forms import PasswordInput
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from django.views import View
from .models import *
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


class TaskList(LoginRequiredMixin,View):
    def get(self,request):
        tasks = Task.objects.filter(user=self.request.user)
        context = {'tasks':tasks}
        return render(request, 'main/task_index.html', context)

    def post(self, request):
        task = Task.objects.create(
            title=request.POST.get('title')
        )
        task.save()
        return redirect('tasks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)    
        return context

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskDetail(LoginRequiredMixin,View):
    def get(self,request,pk):
        task = Task.objects.get(id=pk)
        context = {'task':task}
        return render(request, 'main/task_list.html', context)

    def post(self, request,pk):
        task = Task.objects.get(id=pk)
        task.body = request.POST.get('title')
        task.save()
        return redirect('tasks')

class TaskDelete(View):
    def get(self,request,pk):
        task = Task.objects.get(id=pk)
        context = {'task':task}
        return render(request, 'main/task_delete.html', context)

    def post(self, request,pk):
        task = Task.objects.get(id=pk)
        task.delete()
        return redirect('tasks')

def loginPage(request): 

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

      

        if user is not None:
            login(request, user)
            return redirect('tasks')

        else: 
            messages.info(request, 'Username Or Password is Incorrect')

    context={}
    return render(request, 'main/login.html', context)


def registerPage(request):
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():

            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account Created!")


            return redirect('login')

 
        
    context={'form':form}
    return render(request, 'main/register.html', context )



def logOut(request):
    logout(request)
    return redirect('login')

def timer(request):
    return render(request, 'main/timer.html')
   
    


