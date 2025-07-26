from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ]

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="todo")
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES)
    deadline = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    media = models.FileField(upload_to='comments', null=True, blank=True)