from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    """
    Form used to create a task
    """
    
    class Meta:
        model =Task
        fields =('task_name','description','user_name','priority','start_time','progress','status')

        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'user_name': forms.HiddenInput()
        }
    
    