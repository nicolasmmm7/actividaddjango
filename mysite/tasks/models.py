from django.db import models
from django.utils import timezone
import datetime
class Task(models.Model):
    name_text = models.CharField(max_length=100)
    description_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    completed = models.BooleanField(default=False)
    close_date = models.DateTimeField("date closed")
    def __str__(self):
        return self.name_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class User(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    def __str__(self):
        return self.user_name
    
    
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name
# Create your models here.
