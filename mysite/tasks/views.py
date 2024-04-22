from django.shortcuts import get_object_or_404, render
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
        task = get_object_or_404(Task, pk=task_id)
        return render(request, "tasks/descrip.html", {"task": task})
    

def complet(request, task_id):
    response = "estas viendo si la tarea fue completada %s."
    return HttpResponse(response % task_id)