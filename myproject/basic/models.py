from django.db import models

# Create your models here.

class UserProfile(models.Model):
    name =models.CharField(max_length = 150)
    age = models.IntegerField()
    city = models.CharField(max_length = 100)
    
class Employee(models.Model):
    emp_name =models.CharField(max_length = 150)
    emp_sal = models.IntegerField()
    emp_email = models.EmailField(unique=True)

class Product(models.Model):
    product_name =models.CharField(max_length = 150)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    total_price = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        self.total_price = self.product_price * self.product_quantity
        super().save(*args,**kwargs)
        