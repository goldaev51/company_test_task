from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    due_date = models.DateTimeField()
    creation_time = models.DateTimeField(default=timezone.now())
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
