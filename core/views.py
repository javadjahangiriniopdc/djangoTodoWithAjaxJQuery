from django.shortcuts import render

# Create your views here.
from core.models import TODO
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'core/todo.html')


def todo_list(request):
    todos = TODO.objects.all()
    return JsonResponse({'todos': list(todos.values())})

@csrf_exempt
def todo_create(request):
    if request.method == 'POST':
        todo_name = request.POST.get('todo_name')
        todo = TODO.objects.filter(name=todo_name)

        if todo.exists():
            return JsonResponse({'status': 'error'})
        todo = TODO.objects.create(name=todo_name)
    return JsonResponse({'todo_name': todo.name, 'status': 'created'})
