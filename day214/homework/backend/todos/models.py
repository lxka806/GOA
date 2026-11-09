from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.TextField()
    task_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks",
        null=True,
        blank=True,
    )