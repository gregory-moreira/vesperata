from django.db import models

class Events(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add= True)
    hour = models.TimeField(auto_now_add= True)
    summary = models.TextField()
    
    def __str__(self):
        return (self.title)