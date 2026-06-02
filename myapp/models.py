from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    def __str__(self):
        return self.name

