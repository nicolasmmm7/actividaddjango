from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.template import loader


def index(request):
    latest_task_list = Task.objects.order_by("-pub_date")[:5]
    template = loader.get_template("tasks/index.html")
    context = {
        "latest_task_list": latest_task_list,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.

def descrip(request, task_id):
    return HttpResponse("estas viendo la tarea %s." % task_id)

def complet(request, task_id):
    response = "estas viendo si la tarea fue completada %s."
    return HttpResponse(response % task_id)