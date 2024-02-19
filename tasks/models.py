from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Edificio(models.Model):
    nombre = models.CharField(max_length=100) 
    numeroPisos = models.IntegerField(input) 
    ubicacion = models.CharField(max_length=100) 
    date = models.DateTimeField(auto_now_add=True) 
    description = models.TextField(blank=True) 
    important = models.BooleanField(default=False) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

#class Task(models.Model):
    tittle = models.CharField(max_length=100) 
    description = models.TextField(blank=True) 
    created = models.DateTimeField(auto_now_add=True) 
    datecomplete = models.DateTimeField(null=True) 
    impotant = models.BooleanField(default=False) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    def __str__(self) :
        return self.tittle + '- by ' + self.user.username
    
