from django.urls import path

from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:task_id>/", views.descrip, name="descrip"),
    path("<int:task_id>/completed/", views.complet, name="complet"),
    path("<int:category_id>/", views.print_category, name="descrip_category"),
    path("category/", views.p_category, name= "category")
]