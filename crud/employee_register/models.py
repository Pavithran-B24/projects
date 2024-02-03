from django.db import models

# Create your models here.
class Jobrole(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=50)
    jobrole = models.ForeignKey(Jobrole, on_delete=models.CASCADE)