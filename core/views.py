from django.shortcuts import render

# Create your views here.
from core.models import TODO
from django.http import JsonResponse


def home(request):
    return render(request, 'core/todo.html')


def todo_list(request):
    todos = TODO.objects.all()
    return JsonResponse({'todos':list(todos.values())})
