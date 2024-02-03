from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    job_desc = models.CharField(max_length=50)

    def __str__(self):
        return self.name