from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages


# Create your views here.
def show_task(request, task_id):
    retrieved_task = get_object_or_404(Task, id=task_id)

    context = {
        "task": retrieved_task,
    }

    return render(request, 'tasks/view_task.html', context)

def show_homepage(request):
    return render(request, 'tasks/index.html')  

def create_task(request):
    if request.method =="POST":
        form = TaskForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, "Task Saved!")
            return redirect("home")
      
    else:
        #handle a GET Request
        form = TaskForm()
        context = {
            "form": form,
        }
        return render(request, 'tasks/create_task.html', context)
