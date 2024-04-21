from django.db import models
from django.utils import timezone
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
# Create your models here.
