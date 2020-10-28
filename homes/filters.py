from django.db.models import QuerySet

def filter_price(queryset, price_value, price_select):
    price_int = int(price_value)
    if price_select == 'Less than':
        queryset = queryset.filter(Price__lt=price_int)
    if price_select == 'Greater than':
        queryset = queryset.filter(Price__gt=price_int)
    elif price_select == "Equal to":
        queryset = queryset.filter(Price = price_int)
    return queryset