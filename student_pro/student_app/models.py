from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name=models.CharField(max_length=255)
    employee_address=models.TextField()
    employee_phone_number=models.CharField(max_length=10)
    employee_email=models.EmailField()    

