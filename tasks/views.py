from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth import authenticate, login

          


def HomePage(request):
    """
    Renders the landing page, giving option to sign in
     or start managing tasks if logged in.
    """
    return render(request, 'tasks/index.html')


@login_required
def show_task(request, task_id):
    """
    Retrieves and displays a specific task.
    Ensures that only the task owner can view the task.
    """
    retrieved_task = get_object_or_404(Task, id=task_id)
    # Check if the logged-in user is the owner of the task
    if retrieved_task.user_name != request.user:
        # Handle unauthorized access
        # rediectes to task page if user does not own the task
        return redirect('tasks')
    context = {
        "task": retrieved_task,
        }
    return render(request, 'tasks/view_task.html', context)


@login_required
def show_task_page(request):
    """
    Displays a list of all tasks that a logged in user has created.

    """
    all_tasks = Task.objects.all()
    context = {
        "tasks": all_tasks,
    }
    return render(request, 'tasks/tasks.html', context)
    template_name = "task/tasks.html"
    paginate_by = 6




@login_required
def create_task(request):
    """
    Handles creating a new task for a logged in user
    redirects to task list
    """
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            user_name = request.user
            form.save()
            messages.success(request, "Your task is Saved!")
            return redirect("tasks")
    else:
        # Prepopulate user_name
        form = TaskForm(initial={'user_name': request.user})
        context = {"form": form, }
        return render(request, 'tasks/create_task.html', context)


@login_required
def edit_task(request, task_id):
    """
    Edits an existing task, only logged in users can edit
    redirects to task list
    """
    retrieved_task = get_object_or_404(Task, id=task_id)

    # Check if the logged-in user is the owner of the task
    if retrieved_task.user_name != request.user:
        # Handle unauthorized access
        # rediectes to task page if user does not own the task
        return redirect('tasks')

    if not request.user == retrieved_task.user_name and not request.user.is_superuser:
        messages.error(request, "You can not edit a task that you did not create")
        return redirect("tasks")

    if request.method == "POST":
        form = TaskForm(request.POST, instance=retrieved_task)
        if form.is_valid():
            form.save()
            messages.success(request, "Your task is updated!")
            return redirect("tasks")
    else:
        form = TaskForm(instance=retrieved_task)
        context = {"form": form, }
        return render(request, 'tasks/edit_task.html', context)


@login_required
def delete_task(request, task_id):
    """
    Deletes a task for a logged in user
    redirects to task list
    """
    retrieved_task = get_object_or_404(Task, id=task_id)

    if not request.user == retrieved_task.user_name and not request.user.is_superuser:
        messages.error(request, "You can not delete a task that you did not create")
        return redirect("tasks")

    if request.method == "POST":
        retrieved_task.delete()
        messages.success(request, "Your task was deleted")
        return redirect("tasks")
    else:
        context = {"task": retrieved_task, }
        return render(request, 'tasks/delete_task.html', context)    
        