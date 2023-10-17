from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
  
class Insctructure(models.Model):
    name =   models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    def __str__(self):
        return self.name

    
class Course(models.Model):
    name = models.CharField(max_length=50)
    rating = models.IntegerField(default=0)
    Insctructure = models.ForeignKey(Insctructure,on_delete=models.CASCADE,related_name='courses')

    def __str__(self):
        return self.name


