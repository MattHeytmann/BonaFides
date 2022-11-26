from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subject/<str:pk>', views.subject, name='subject'),
    path('login/', views.loginUser, name='log-in'),
    path('logout/', views.logoutUser, name='log-out'),
    path('list/<str:pk>', views.list, name='list'),
    path('excercise/<str:pk>', views.excercise, name='excercise'),
    path('test/<str:pk>', views.test, name='test'),
]