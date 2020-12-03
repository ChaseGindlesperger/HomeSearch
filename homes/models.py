from django.db import models

# Create your models here.


class Amenities(models.Model):
    Address = models.CharField(max_length=50)
    Laundry = models.CharField(null = False, default='N/A', max_length=50, choices=[('None', 'None'), ('Room', 'Room'), ('Building','Building')])
    Kitchen = models.CharField(null = False, default='N/A', max_length=50, choices=[('None', 'None'), ('Half', 'Half'), ('Full', 'Full')])
    CommonAreas =models.CharField(null = False, default='N/A', max_length=50, choices=[('None', 'None'), ('Few', 'Few'), ('Many', 'Many')])
    AC = models.CharField(null = False, default='N/A', max_length=50, choices=[('None', 'None'), ('Central', 'Central'), ('Window', 'Window')])
    Furnished = models.BooleanField(null = False)
    InternetTV = models.BooleanField(null = False)
    def __str__(self):
        return self.Address

class House(models.Model):
    amenities = models.ForeignKey(Amenities, on_delete= models.CASCADE)
    Address = models.CharField(max_length=50)
    Bedrooms = models.IntegerField(null= False)
    Bathrooms = models.DecimalField(null = False, max_digits = 2, decimal_places = 1)
    Price = models.IntegerField(null = False)
    Safety = models.CharField(null = False, default='N/A', max_length=50, choices=[('Least Safe', 'Least Safe'), ('Less Safe', 'Less Safe'), ('More Safe', 'More Safe'), ('Most Safe', 'Most Safe')])
    image = models.ImageField(upload_to='images/', default='default.jpg')
    def __str__(self):
        return self.Address

class Apartment(models.Model):
    amenities = models.ForeignKey(Amenities, on_delete= models.CASCADE)
    Address = models.CharField(max_length=50)
    Name = models.CharField(max_length=50, null= False)
    Bedrooms = models.IntegerField(null= False)
    Bathrooms = models.DecimalField(null = False, max_digits = 2, decimal_places = 1)
    Price = models.IntegerField(null = False)
    Safety = models.CharField(null = False, default='N/A', max_length=50, choices=[('Least Safe', 'Least Safe'), ('Less Safe', 'Less Safe'), ('More Safe', 'More Safe'), ('Most Safe', 'Most Safe')])
    image = models.ImageField(upload_to='images/', default='default.jpg')
    def __str__(self):
        return self.Name

class Food(models.Model):
    Address = models.CharField(max_length=50)
    Name = models.CharField(max_length=50, null = False)
    def __str__ (self):
        return self.Address

class Dorms(models.Model):
    amenities = models.ForeignKey(Amenities, on_delete= models.CASCADE)
    Address = models.CharField(max_length=50)
    Name = models.CharField(max_length=50, null= False)
    Roomstyle = models.CharField(null = False, default='N/A', max_length=50, choices=[('Single', 'Single'), ('Shared Single', 'Shared Single'), ('Double', 'Double'), ('Triple', 'Triple'), ('Suite', 'Suite'), ('Apartment', 'Apartment')])
    Bathrooms = models.CharField(null = False, default='N/A', max_length=50, choices=[('Private', 'Private'), ('Communal', 'Communal')])
    Price = models.IntegerField(null = False)
    Safety = models.CharField(null = False, default='N/A', max_length=50, choices=[('Least Safe', 'Least Safe'), ('Less Safe', 'Less Safe'), ('More Safe', 'More Safe'), ('Most Safe', 'Most Safe')])
    image = models.ImageField(upload_to='images/', default='default.jpg')
    def __str__(self):
        return self.Name