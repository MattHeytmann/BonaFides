from django.contrib import admin
from . models import Subject, Lesson, Question

# Register your models here.

admin.site.register(Question)
admin.site.register(Lesson)
admin.site.register(Subject)