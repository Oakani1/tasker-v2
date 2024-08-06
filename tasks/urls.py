from django.urls import path
from . import views

urlpatterns = [
    path("read/<task_id>", views.show_task, name="read")
]