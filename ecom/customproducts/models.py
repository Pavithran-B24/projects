from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CustomProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.BigIntegerField(max)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)