from unicodedata import name
from django.db import models

# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table="categories"
        verbose_name="category"
        verbose_name_plural="categories"