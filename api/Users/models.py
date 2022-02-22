from pyexpat import model
from tabnanny import verbose
from unicodedata import name
from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta():
        db_table='users'
        verbose_name='user'
        verbose_name_plural='users'