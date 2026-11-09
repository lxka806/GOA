from django.db import models
from django.conf import settings


class Task(models.Model):
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    task_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title