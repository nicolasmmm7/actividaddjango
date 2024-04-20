from django.db import models

class Task(models.Model):
    name_text = models.CharField(max_length=100)
    description_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    completed = models.BooleanField(default=False)
    close_date = models.DateTimeField("date closed")
# Create your models here.
