from django.db import models

# Create your models here.
# from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    photo = models.ImageField(upload_to='photo/')
    resume = models.FileField(upload_to='resume/')
