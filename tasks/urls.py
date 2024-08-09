from django.urls import path
from . import views

urlpatterns = [
    #path("", views.Homepage.as_view(), name="home"),
    path("", views.HomePage, name="home"),
    path("view/<task_id>", views.show_task, name="view"),
    path("task", views.show_task_page, name="task"),
    path("create/", views.create_task, name="create"),
    path("edit/<task_id>", views.edit_task, name="edit"),
    path("delete/<task_id>", views.delete_task, name="delete"),

]