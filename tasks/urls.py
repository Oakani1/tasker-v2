from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.HomePage, name="home"),
    path("tasks", views.show_task_page, name="tasks"),
    path("tasks/create", views.create_task, name="create"),
    path("tasks/edit/<task_id>", views.edit_task, name="edit"),
    path("tasks/delete/<task_id>", views.delete_task, name="delete"),

    path("", views.HomePage, name="home"),
    path("tasks/", views.show_task_page, name="tasks"),
    path("tasks/create/", views.create_task, name="create"),
    path("tasks/edit/<task_id>/", views.edit_task, name="edit"),
    path("tasks/delete/<task_id>/", views.delete_task, name="delete"),

]