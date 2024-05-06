from django.test import TestCase, Client
from django.urls import reverse
from .models import Task, Category, User
import json

class TasksCompletedListTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.task1 = Task.objects.create(name_text="Tarea 1", description_text="Descripción de la tarea 1", completed=True)
        self.task2 = Task.objects.create(name_text="Tarea 2", description_text="Descripción de la tarea 2", completed=False)

    def test_tasks_completed_list(self):
        response = self.client.get(reverse("tasks:tasks_completeds"))
        self.assertEqual(response.status_code, 200)
        task_data = json.loads(response.content)
        self.assertEqual(len(task_data), 1)  # Debería haber solo una tarea completada
        self.assertEqual(task_data[0]["name"], "Tarea 1")
        self.assertEqual(task_data[0]["completed?"], True)
# Create your tests here.
