# todo_app/views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Task
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        data = [{"id": task.id, "title": task.title, "description": task.description, "due_date": task.due_date} for task in tasks]
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        task = Task.objects.create(title=data['title'], description=data.get('description'), due_date=data.get('due_date'))
        return JsonResponse({"message": "Task created successfully", "id": task.id}, status=201)

@csrf_exempt
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'GET':
        data = {"id": task.id, "title": task.title, "description": task.description, "due_date": task.due_date}
        return JsonResponse(data)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.due_date = data.get('due_date', task.due_date)
        task.save()
        return JsonResponse({"message": "Task updated successfully"})

    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({"message": "Task deleted successfully"}, status=204)

