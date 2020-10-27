from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Amenities(models.Model):
    Address = models.CharField(max_length=50, primary_key=True)
    Laundry = models.CharField(max_length=50, null = False)
    Kitchen = models.CharField(max_length=50, null = False)
    InternetTV = models.CharField(max_length=50, null = False)
    CommonAreas = models.CharField(max_length=50, null = False)
    AC = models.CharField(max_length=50, null = False)
    Furnished = models.BooleanField(null = False)
    def __str__(self):
        return self.Address

class House(models.Model):
    Address = models.ForeignKey(Amenities, on_delete= models.CASCADE)
    Name = models.CharField(max_length=50, null= False)
    Bedrooms = models.IntegerField(null= False)
    Bathrooms = models.DecimalField(null = False, max_digits = 2, decimal_places = 1)
    Price = models.IntegerField(null = False)
    Safety = models.IntegerField(null = False)
    image = models.ImageField(upload_to='images/', default='default.jpg')
    def __str__(self):
        return self.Name

class Apartment(models.Model):
    Address = models.ForeignKey(Amenities, on_delete= models.CASCADE)
    Name = models.CharField(max_length=50, null= False)
    Bedrooms = models.IntegerField(null= False, primary_key= True)
    Bathrooms = models.DecimalField(null = False, max_digits = 2, decimal_places = 1)
    Price = models.IntegerField(null = False)
    Safety = models.IntegerField(null = False)
    image = models.ImageField(upload_to='images/', default='default.jpg')
    def __str__(self):
        return self.Name

class Food(models.Model):
    Address = models.CharField(max_length=50, primary_key= True)
    Name = models.CharField(max_length=50, null = False)
    def __str__ (self):
        return self.Name

class Dorms(models.Model):
    Address = models.ForeignKey(Amenities, on_delete= models.CASCADE)
    Name = models.CharField(max_length=50, null= False)
    Roomstyle = models.CharField(max_length=50, null= False)
    Bathrooms = models.CharField(max_length=50, null= False)
    Price = models.IntegerField(null = False)
    Safety = models.IntegerField(null = False)
    image = models.ImageField(upload_to='images/', default='default.jpg')
    def __str__(self):
        return self.Name
