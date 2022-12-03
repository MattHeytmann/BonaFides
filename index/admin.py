from django.contrib import admin
from . models import Subject, Lesson, Question, PrivateSubject, PrivateLesson, PrivateQuestion

# Register your models here.

admin.site.register(Question)
admin.site.register(Lesson)
admin.site.register(Subject)
admin.site.register(PrivateQuestion)
admin.site.register(PrivateLesson)
admin.site.register(PrivateSubject)