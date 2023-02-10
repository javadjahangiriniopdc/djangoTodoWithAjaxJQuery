from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo-list/', views.todo_list, name='todo-list')
]
