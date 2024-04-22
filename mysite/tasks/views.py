from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.template import loader
from django.http import Http404

def index(request):
    latest_task_list = Task.objects.order_by("-pub_date")[:5]
    context = {
        "latest_task_list": latest_task_list,
    }
    return render(request, "tasks/index.html", context)

# Create your views here.

def descrip(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "tasks/descrip.html", {"task": task})

def complet(request, task_id):
    response = "estas viendo si la tarea fue completada %s."
    return HttpResponse(response % task_id)