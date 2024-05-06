from django.urls import path

from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:task_id>/", views.descrip, name="descrip"),
    path("task_completed/", views.tasks_completed_list, name="tasks_completeds"),
    path("category/", views.category_list, name= "category"),
    path("user/", views.user_list, name= "user")
]