from django.db import models
from mptt.models import MPTTModel,TreeForeignKey
# Create your models here.
class Category(MPTTModel):
    name=models.CharField(max_length=255)
    parent=TreeForeignKey("self",on_delete=models.PROTECT,null=True,blank=True)
    
    class MPTTMetta:
        order_insertion_by=['name']
    
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class products(models.Model):
    name=models.CharField(max_length=255)
    discription=models.CharField(max_length=255,blank=True)
    brand=models.ForeignKey(Brand, null=True, on_delete=models.CASCADE)
    category=TreeForeignKey(Category, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name