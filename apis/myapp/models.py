from django.db import models

# Create your models here.


class Student(models.Model):
    rollno = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    marks = models.IntegerField()

    # def __str__(self) -> str:
    #     return self.title