from django.db import models

# Create your models here.
""" class AdminModel(models.Model):
    username = models.CharField(max_length= 10)
    password = models.CharField(max_length= 10) """
class PizzaModel(models.Model):
    name = models.CharField(max_length= 10)
    price = models.CharField(max_length= 10)

class CustomerModel(models.Model) :
    userid = models.CharField(max_length= 10)
    phoneno = models.CharField(max_length= 10)

class OrderModel(models.Model):
    username = models.CharField(max_length= 10)
    phoneno = models.CharField(max_length= 10)
    address = models.CharField(max_length= 10)
    ordereditems = models.CharField(max_length= 30)
    status = models.CharField(max_length= 10)
