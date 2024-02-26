# models.py

from django.db import models


class EventCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='event_category_images/')

    def __str__(self):
        return self.name
    
    
class EventService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
 

    def __str__(self):
        return self.name
    
    