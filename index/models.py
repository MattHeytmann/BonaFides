from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    lesson = models.ForeignKey("Lesson", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title + ' | ' + self.description

class Lesson(models.Model):
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title + ' | ' + self.description

class Subject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title + ' | ' + self.description
