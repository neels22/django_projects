from django.db import models

# Create your models here.
class Employee(models.Model):
    designation = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    joining_date = models.DateField()

    def __str__(self) -> str:
        return "Employee name: "+ self.name
    