from django.db import models

# Create your models here.

class Student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField(null = True, blank= True)
    address = models.TextField(null = True, blank= True)
    # image = models.ImageField(null = True, blank= True)
    # file = models.FileField(null = True, blank= True)

class Car(models.Model):
    name = models.CharField(max_length = 500)
    speed = models.IntegerField(default= 50)


    def __str__(self) -> str:
        return self.name