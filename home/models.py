from django.db import models

# Create your models here.

class Student(models.Model):
    # id = models.AutoField() this is django default/primary key bhi
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Email = models.EmailField()
    Address = models.TextField()
    Image = models.ImageField()
    file = models.FileField()


class Car(models.Model):
    car_name= models.CharField(max_length=100)
    speed = models.IntegerField(default=50)
    
    def __str__(self) -> str:
        return self.car_name