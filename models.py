# todo_app/models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

