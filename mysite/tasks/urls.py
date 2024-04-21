from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:task_id>/", views.descrip, name="descrip"),
    path("<int:task_id>/completed/", views.complet, name="complet"),
]