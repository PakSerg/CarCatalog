import django_filters
from .models import Car


class CarFilter(django_filters.FilterSet): 
    brand = django_filters.CharFilter(lookup_expr='iexact')
    model = django_filters.CharFilter(lookup_expr='iexact')
    year = django_filters.NumberFilter()
    fuel_type = django_filters.CharFilter(lookup_expr='iexact')
    transmission = django_filters.CharFilter(lookup_expr='iexact')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    mileage_min = django_filters.NumberFilter(field_name='mileage', lookup_expr='gte')
    mileage_max = django_filters.NumberFilter(field_name='mileage', lookup_expr='lte')

    class Meta:
        model = Car 
        fields = ['brand', 'model', 'year', 'fuel_type', 'transmission'] 
