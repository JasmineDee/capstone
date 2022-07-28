from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .models import Task
from django.views import View


# Create your views here.

class TaskList(View):
    def get(self,request):
        tasks = Task.objects.all()
        context = {'tasks':tasks}
        return render(request, 'main/task_index.html', context)

    def post(self, request):
        task = Task.objects.create(
            title=request.POST.get('title')
        )
        task.save()
        return redirect('tasks')

class TaskDetail(View):
    def get(self,request,pk):
        task = Task.objects.get(id=pk)
        context = {'task':task}
        return render(request, 'main/task_list.html', context)

    def post(self, request,pk):
        task = Task.objects.get(id=pk)
        task.body = request.POST.get('body')
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
