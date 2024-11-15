from django.db import models
import os

from django.contrib.auth.models import User


# Create your models here.

class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True )
    name = models.CharField(max_length= 100)
    description = models.TextField()
    image = models.ImageField(upload_to="receipe")
    view_count = models.IntegerField(default=1)


    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

  
class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering=['department']

class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id
    
class Student(models.Model):
    department = models.ForeignKey(Department, related_name= "depaart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name="studentid", on_delete=models.SET_NULL, null=True)
    student_name = models.CharField(max_length= 100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default = 18)
    student_address = models.TextField()

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = "student"

