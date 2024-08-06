from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Pending"), (1, "In progress"), (2, "Complete"), (3, "Late"))

class Task(models.Model):
    task_name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(blank=True)
    user_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="task"
    )
    start_time = models.DateTimeField(null=False, blank=False)
    progress = models.IntegerField(null=False, blank=False)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__ (self):
        return f'{self.task_name}'