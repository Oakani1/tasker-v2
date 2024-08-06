from django.shortcuts import render
from .models import Task

# Create your views here.
def show_task(request, task_id):
    retrieved_task = get_object_or_404(Task, id=task_id)
