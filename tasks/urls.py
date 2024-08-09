from django.urls import path
from . import views

urlpatterns = [
    #path("", views.Homepage.as_view(), name="home"),
    path("", views.HomePage, name="home"),
    path("signin/", views.SignInPage, name="signin"),
    path("signup/", views.SignUpPage, name="signup"),
    path("tasks/view/<task_id>", views.show_task, name="view"),
    path("tasks/", views.show_task_page, name="tasks"),
    path("tasks/create/", views.create_task, name="create"),
    path("tasks/edit/<task_id>", views.edit_task, name="edit"),
    path("tasks/delete/<task_id>", views.delete_task, name="delete"),

]