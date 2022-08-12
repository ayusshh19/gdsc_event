
from django.db import models

# Create your models here.
class Eventmanage(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)
    date=models.DateField()
    time=models.TimeField()
    
    def __str__(self):
        return self.name
