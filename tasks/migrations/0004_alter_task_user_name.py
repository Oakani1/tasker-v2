# Generated by Django 4.2.14 on 2024-08-13 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0003_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task', to=settings.AUTH_USER_MODEL),
        ),
    ]
