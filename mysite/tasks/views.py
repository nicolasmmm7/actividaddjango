from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from .models import Task, Category, User
from django.template import loader
from django.http import Http404

def index(request):
    latest_task_list = Task.objects.order_by("-pub_date")[:5]
    context = {
        "latest_task_list": latest_task_list,
    }
    return render(request, "tasks/index.html", context)

def p_category(request):
    latest_category_list = Category.objects.all()
    context = {
        "latest_category_list": latest_category_list,
    }
    return render(request, "tasks/category/categorias.html", context)

def p_user(request):
    latest_user_list = User.objects.all()
    context = {
        "latest_user_list": latest_user_list,
    }
    return render(request, "tasks/user/usuarios.html", context)

def user_list(request):
    users = User.objects.all()
    user_data = [{"name": user.user_name, "email": user.email, "phone": user.phone_number} for user in users]
    return JsonResponse(user_data, safe=False)

def category_list(request):
    categorys = Category.objects.all()
    category_data = [{"name": category.category_name, "description": category.description} for category in categorys]
    return JsonResponse(category_data, safe=False)


def descrip(request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        return render(request, "tasks/descrip.html", {"task": task})
    
    

def complet(request, task_id):
    response = "estas viendo si la tarea fue completada %s."
    return HttpResponse(response % task_id)