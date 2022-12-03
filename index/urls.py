from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subject/<str:pk>', views.subject, name='subject'),
    path('login/', views.loginUser, name='log-in'),
    path('logout/', views.logoutUser, name='log-out'),
    path('list/<str:pk>', views.llist, name='list'),
    path('excercise/<str:pk>', views.excercise, name='excercise'),
    path('test/<str:pk>', views.test, name='test'),
    path('privateSubject/<str:pk>', views.privateSubject, name='privateSubject'),
    path('privateList/<str:pk>', views.privateList, name='privateList'),
    path('privateExcercise/<str:pk>', views.privateExcercise, name='privateExcercise'),
    path('privateTest/<str:pk>', views.privateTest, name='privateTest'),
    path('newPrivateSubject', views.privateSubjectCreate, name='privateSC'),
    path('newPrivateLesson/<str:pk>', views.privateLessonCreate, name='privateLC'),
    path('privateSubject/<str:pk>/delete', views.deleteSubject, name='deleteSubject'),
    path('privateList/<str:pk>/delete', views.deleteLesson, name='deleteLesson'),
    path('question/<str:pk>/delete', views.deleteQuestion, name='deleteQuestion'),
]