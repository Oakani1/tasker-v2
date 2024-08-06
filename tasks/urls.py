from django.urls import path
from . import views

urlpatterns = [
    path("view/<task_id>", views.show_task, name="view"),
    path("homepage/", views.show_homepage, name="home"),
    path("create/", views.create_task, name="create"),
]