from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")
# Create your views here.

def descrip(request, task_id):
    return HttpResponse("estas viendo la tarea %s." % task_id)

def complet(request, task_id):
    response = "estas viendo si la tarea fue completada %s."
    return HttpResponse(response % task_id)