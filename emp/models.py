from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

# 'file': ['logo.jfif'], 
# 'emp_name': ['aKEE'], 
# 'emp_gender': ['Male'], 
# 'emp_age': ['12'],
# 'emp_religion': ['Muslim'], 
# 'emp_phone': ['08063641230'], 
# 'emp_qualification': ['HHJHJHJJHHJK'], 
# 'emp_experience': ['JHHJHJHHJK'], 
# 'emp_client': ['DSKJDKJL'], 
# 'emp_working': ['2024-12-31'], 
# 'emp_department': ['ME']

class Emp(models.Model):
    name=models.CharField(max_length=200)
    age= models.CharField(max_length=10, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    phone=models.CharField(max_length=40, blank=True)
    department=models.CharField(max_length=200, blank=True)
    religion=models.CharField(max_length=20)
    qualification=models.TextField(blank=True)
    client=models.CharField(max_length=100, blank=True)
    experience =models.TextField(blank=True)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True)
    date_startwork = models.DateField()
    
    def __str__(self):
        return self.name

