from itertools import chain
from django.shortcuts import render
from django.db.models import QuerySet
from homes.models import House, Apartment, Dorms, Amenities

# Create your views here.

def index(request):
    return render(request, 'homes/index.html')

def search(request):
    houses = QuerySet()
    apartments = QuerySet()
    dorms = QuerySet()
    result = render(request, 'homes/index.html')
    if request.method == 'GET':
        if 'search' in request.GET:
            search_value = request.GET.get('search')
            if search_value is not None and search_value != '':
                result = Apartment.objects.filter(Address__Address__icontains = search_value)
    return result