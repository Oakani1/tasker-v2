from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model =Task
        fields = ('task_name', 'description', 'priority', 'user_name', 'start_time', 'progress', 'status')
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }