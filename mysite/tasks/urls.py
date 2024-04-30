from django.urls import path

from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:task_id>/", views.descrip, name="descrip"),
    path("<int:task_id>/completed/", views.complet, name="complet"),
    path("category/", views.p_category, name= "category"),
    path("user/", views.p_user, name= "user")
]