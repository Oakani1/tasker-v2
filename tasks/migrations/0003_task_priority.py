# Generated by Django 4.2.14 on 2024-08-07 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_rename_user_id_task_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.IntegerField(choices=[(0, 'Low'), (1, 'Medium'), (2, 'High')], default=0),
        ),
    ]