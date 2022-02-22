from django.db import models
from api.Categories.models import Categories

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()
    category = models.ForeignKey(Categories, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table="products"
        verbose_name='product'
        verbose_name_plural="products"
