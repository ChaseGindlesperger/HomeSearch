from django.contrib import admin
from .models import House, Apartment, Amenities, Food

# Register your models here.

admin.site.register(House)
admin.site.register(Apartment)
admin.site.register(Amenities)
admin.site.register(Food)
