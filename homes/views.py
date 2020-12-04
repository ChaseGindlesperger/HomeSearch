from itertools import chain
from django.core import serializers
from django.shortcuts import render
from django.db.models import QuerySet
from homes.models import House, Apartment, Dorms, Food
from . import filters

# Create your views here.


def homepage(request):
    return render(request, 'homes/homepage.html')


def index(request):
    return render(request, 'homes/index.html')


def info(request):
    home = request.GET.get('home')
    if House.objects.filter(Address=home).count():
        data = House.objects.get(Address=home)
    elif Apartment.objects.filter(Name=home).count() > 0:
        data = Apartment.objects.get(Name=home)
    elif Dorms.objects.filter(Name=home).count() > 0:
        data = Dorms.objects.get(Name=home)
    food = Food.objects.all()
    food_list = serializers.serialize('json', food)
    #food_list = food[::1]
    #food_list = model_to_dict(food)
    #json_list = json.dumps(food_list)
    return render(request, 'homes/info.html', {'home': data, 'food_list': food})


def search(request):
    houses = QuerySet()
    apartments = QuerySet()
    dorms = QuerySet()
    search_value = ''
    price_value = ''
    price_select = ''
    price_bool = False
    bedroom_bool = False
    laundry_bool = False
    kitchen_bool = False
    AC_bool = False
    commonareas_bool = False
    if request.method == "GET":
        bedroom_value = request.GET.get('bedroomselect')
        if bedroom_value is not None and bedroom_value != '' and bedroom_value != 'Any':
            bedroom_bool = True
        laundry_value = request.GET.get('laundry')
        if laundry_value is not None and laundry_value != '' and laundry_value != 'Any':
            laundry_bool = True
        price_value = request.GET.get('price')
        price_select = request.GET.get('priceselect')
        if price_value is not None and price_value != '':
            price_bool = True
        kitchen_value = request.GET.get('kitchen')
        if kitchen_value is not None and kitchen_value != '' and kitchen_value != 'Any':
            kitchen_bool = True
        AC_value = request.GET.get('AC')
        if AC_value is not None and AC_value != '' and AC_value != 'Any':
            AC_bool = True
        commonareas_value = request.GET.get('commonareas')
        if commonareas_value is not None and commonareas_value != '' and commonareas_value != 'Any':
            commonareas_bool = True
        if 'search' in request.GET:
            if request.GET.get('search') is not None and request.GET.get('search') != '':
                search_value = request.GET.get('search')
        if 'type' in request.GET:
            type_value = request.GET.get('type')
            if type_value is not None and type_value != '':
                if type_value == 'House':
                    houses = House.objects.filter(Address__icontains=search_value)
                    if price_bool:
                        houses = filters.filter_price(houses, price_value, price_select)
                    if bedroom_bool:
                        houses = houses.filter(Bedrooms=bedroom_value)
                    if laundry_bool:
                        houses = houses.filter(amenities__Laundry=laundry_value)
                    if kitchen_bool:
                        houses = houses.filter(amenities__Kitchen=kitchen_value)
                    if AC_bool:
                        houses = houses.filter(amenities__AC=AC_value)
                    if commonareas_bool:
                        houses = houses.filter(amenities__CommonAreas=commonareas_value)
                    result = render(request, 'homes/searchresults.html', {'homes_list': houses})
                elif type_value == 'Apartment':
                    apartments = Apartment.objects.filter(Address__icontains=search_value)
                    if price_bool:
                        apartments = filters.filter_price(apartments, price_value, price_select)
                    if bedroom_bool:
                        apartments = apartments.filter(Bedrooms=bedroom_value)
                    if laundry_bool:
                        apartments = apartments.filter(amenities__Laundry=laundry_value)
                    if kitchen_bool:
                        apartments = apartments.filter(amenities__Kitchen=kitchen_value)
                    if AC_bool:
                        apartments = apartments.filter(amenities__AC=AC_value)
                    if commonareas_bool:
                        apartments = apartments.filter(amenities__CommonAreas=commonareas_value)
                    result = render(request, 'homes/searchresults.html', {'homes_list': apartments})
                elif type_value == 'Dorm':
                    dorms = Dorms.objects.filter(Address__icontains=search_value)
                    if price_bool:
                        dorms = filters.filter_price(dorms, price_value, price_select)
                    if laundry_bool:
                        dorms = dorms.filter(amenities__Laundry=laundry_value)
                    if kitchen_bool:
                        dorms = dorms.filter(amenities__Kitchen=kitchen_value)
                    if AC_bool:
                        dorms = dorms.filter(amenities__AC=AC_value)
                    if commonareas_bool:
                        dorms = dorms.filter(amenities__CommonAreas=commonareas_value)
                    result = render(request, 'homes/searchresults.html', {'homes_list': dorms})
                else:
                    houses = House.objects.filter(Address__icontains=search_value)
                    if price_bool:
                        houses = filters.filter_price(houses, price_value, price_select)
                    if bedroom_bool:
                        houses = houses.filter(Bedrooms=bedroom_value)
                    if laundry_bool:
                        houses = houses.filter(amenities__Laundry=laundry_value)
                    if kitchen_bool:
                        houses = houses.filter(amenities__Kitchen=kitchen_value)
                    if AC_bool:
                        houses = houses.filter(amenities__AC=AC_value)
                    if commonareas_bool:
                        houses = houses.filter(amenities__CommonAreas=commonareas_value)
                    apartments = Apartment.objects.filter(Address__icontains=search_value)
                    if price_bool:
                        apartments = filters.filter_price(apartments, price_value, price_select)
                    if bedroom_bool:
                        apartments = apartments.filter(Bedrooms=bedroom_value)
                    if laundry_bool:
                        apartments = apartments.filter(amenities__Laundry=laundry_value)
                    if kitchen_bool:
                        apartments = apartments.filter(amenities__Kitchen=kitchen_value)
                    if AC_bool:
                        apartments = apartments.filter(amenities__AC=AC_value)
                    if commonareas_bool:
                        apartments = apartments.filter(amenities__CommonAreas=commonareas_value)
                    dorms = Dorms.objects.filter(Address__icontains=search_value)
                    if price_bool:
                        dorms = filters.filter_price(dorms, price_value, price_select)
                    if laundry_bool:
                        dorms = dorms.filter(amenities__Laundry=laundry_value)
                    if kitchen_bool:
                        dorms = dorms.filter(amenities__Kitchen=kitchen_value)
                    if AC_bool:
                        dorms = dorms.filter(amenities__AC=AC_value)
                    if commonareas_bool:
                        dorms = dorms.filter(amenities__CommonAreas=commonareas_value)
                    queryset = chain(houses, apartments, dorms)
                    sortedSet = sorted(queryset, key=lambda x: (x.Price, x.Address))
                    result = render(request, 'homes/searchresults.html', {'homes_list': sortedSet})
    return result
