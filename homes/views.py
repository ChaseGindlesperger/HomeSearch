from django.shortcuts import render
from django.http import HttpResponse
from homes.models import House, Apartment, Food, Amenities

# Create your views here.

def index(request):
    context = {}
    return render(request, 'homes/index.html', context)

def search(request):
    if request.method == "GET":
        search_value = request.GET.get('search')
        queryset = Apartment.objects.filter(Name__icontains = search_value)
        return render(request, 'homes/searchresults.html', {'homes_list': queryset})