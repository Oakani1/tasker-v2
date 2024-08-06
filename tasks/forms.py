from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model =Task
        fields = ('task_name', 'description', 'user_name', 'start_time', 'progress', 'status')