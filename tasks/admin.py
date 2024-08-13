from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Task
# Register your models here.

@admin.register(Task)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('task_name', 'user_name', 'description', 'priority', 'status')
    search_fields = ['task_name']
    list_filter = ('status',)
    prepopulated_fields = {'task_name': ('status',)}
    summernote_fields = ('description',)

