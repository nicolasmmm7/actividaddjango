from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def index(request):
    latest_task_list = Task.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.name_text for q in latest_task_list])
    return HttpResponse(output)

# Create your views here.

def descrip(request, task_id):
    return HttpResponse("estas viendo la tarea %s." % task_id)

def complet(request, task_id):
    response = "estas viendo si la tarea fue completada %s."
    return HttpResponse(response % task_id)