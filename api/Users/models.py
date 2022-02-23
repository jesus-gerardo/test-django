from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    photo = models.ImageField(null=True, upload_to='users')

    # USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.name

    class Meta():
        db_table='users'
        verbose_name='user'
        verbose_name_plural='users'