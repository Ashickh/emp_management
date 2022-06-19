from django.db import models

# Create your models here.

class Employee(models.Model):
    eid=models.CharField(max_length=30,primary_key=True)
    emp_name=models.CharField(max_length=120)
    desig=models.CharField(max_length=120)
    salary=models.PositiveIntegerField()
    email=models.EmailField(unique=True)
    experience=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.emp_name
