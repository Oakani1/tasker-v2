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
            messages.success(request, "Your task is Saved!")
            return redirect("home")
      
    else:
        #handle a GET Request
        form = TaskForm()
        context = {"form": form, }
        return render(request, 'tasks/create_task.html', context)

def edit_task(request, task_id):
    retrieved_task = get_object_or_404(Task, id=task_id)

    if not request.user == retrieved_task.user_name:
        messages.error(request, "You can not edit a task that you did not create")
        return redirect("home")

    if request.method =="POST":
        
        form = TaskForm(request.POST, instance=retrieved_task)
        if form.is_valid() :
            form.save()
            messages.success(request, "Your task is updated!")
            return redirect("home")
      
    else:   
        form = TaskForm(instance=retrieved_task)
        context = {"form": form, }
        return render(request, 'tasks/edit_task.html', context)

def delete_task(request, task_id):
    retrieved_task = get_object_or_404(Task, id=task_id)

    if not request.user == retrieved_task.user_name:
        messages.error(request, "You can not delete a task that you did not create")
        return redirect("home")

    if request.method =="POST":
        retrieved_task.delete()
        messages.success(request, "Your task was deleted")
        return redirect("home")
      
    else:   
        context = {"task": retrieved_task, }
        return render(request, 'tasks/delete_task.html', context)    
        