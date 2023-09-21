from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    seller = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    ratings = models.PositiveIntegerField()
    ratingsCount = models.PositiveIntegerField()
    img = models.URLField()
    shipping = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

