from django.contrib import admin
from .models import Task
from .models import User
from .models import Category

admin.site.register(Task)
admin.site.register(User)
admin.site.register(Category)

# Register your models here.
