from itertools import chain
import pdb
from django.shortcuts import render
from django.db.models import QuerySet
from homes.models import House, Apartment, Dorms, Amenities
from . import filters

# Create your views here.

def index(request):
    return render(request, 'homes/index.html')

def search(request):
    houses = QuerySet()
    apartments = QuerySet()
    dorms = QuerySet()
    search_value = ''
    price_value = request.GET.get('price')
    price_select = request.GET.get('priceselect')
    price_bool = False
    if price_value is not None and price_value != '':
        price_bool = True
    if 'type' in request.GET:
        type_value = request.GET.get('type')
        if type_value is not None and type_value != '':
            if type_value == 'House':
                houses = House.objects.filter(Address__icontains=search_value)
                if price_bool:
                    houses = filters.filter_price(houses, price_value, price_select)
                result = render(request, 'homes/searchresults.html', {'homes_list': houses})
            elif type_value == 'Apartment':
                apartments = Apartment.objects.filter(Address__icontains=search_value)
                if price_bool:
                    apartments = filters.filter_price(houses, price_value, price_select)
                result = render(request, 'homes/searchresults.html', {'homes_list': apartments})
            elif type_value == 'Dorm':
                dorms = Dorms.objects.filter(Address__icontains=search_value)
                if price_bool:
                    dorms = filters.filter_price(houses, price_value, price_select)
                result = render(request, 'homes/searchresults.html', {'homes_list': dorms})
            else:
                houses = House.objects.filter(Address__icontains=search_value)
                if price_bool:
                    houses = filters.filter_price(houses, price_value, price_select)
                apartments = Apartment.objects.filter(Address__icontains=search_value)
                if price_bool:
                    apartments = filters.filter_price(houses, price_value, price_select)
                dorms = Dorms.objects.filter(Address__icontains=search_value)
                if price_bool:
                    dorms = filters.filter_price(houses, price_value, price_select)
                queryset = chain(houses, apartments, dorms)
                result = render(request, 'homes/searchresults.html', {'homes_list': queryset})
    return result