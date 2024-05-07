import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
django.setup()
import json
from django.urls import reverse
from django.test import Client
import pytest
from .models import Task


@pytest.mark.django_db
def test_tasks_completed_list():
    # Recuperamos todas las tareas de la base de datos
    all_tasks = Task.objects.all()
    
    # Creamos un cliente de prueba
    client = Client()

    # Hacemos una solicitud a la vista tasks_completed_list
    response = client.get(reverse("tasks:task_completed"))

    # Verificamos que la solicitud haya sido exitosa (código de estado 200)
    assert response.status_code == 200

    # Convertimos el contenido de la respuesta en un diccionario JSON
    task_data = json.loads(response.content)
  
    # Verificamos que solo haya una tarea completada en la respuesta
    assert len(task_data) == len([task for task in all_tasks if task.completed])
    assert len(task_data) != 2

    # Verificamos que la tarea en la respuesta sea la correcta
    for task in task_data:
        assert task["completed"] == True