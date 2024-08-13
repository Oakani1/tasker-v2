from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages

STATUS = ((0, "Pending"), (1, "In progress"), (2, "Complete"), (3, "Late"))
PRIORITY = ((0, "Low"), (1, "Medium"), (2, "High"))


class Task(models.Model):
    task_name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(blank=True)
    priority = models.IntegerField(choices=PRIORITY, default=0)
    user_name = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="task", null=True)
    start_time = models.DateTimeField(null=False, blank=False)
    progress = models.IntegerField(null=False, blank=False)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f'{self.task_name}'