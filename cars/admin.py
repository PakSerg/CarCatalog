from django.contrib import admin


from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'fuel_type', 'transmission', 'mileage', 'price')
    list_filter = ('fuel_type', 'transmission', 'year')
    search_fields = ('brand', 'model', 'year', 'fuel_type', 'transmission')
    fields = ('brand', 'model', 'year', 'fuel_type', 'transmission', 'mileage', 'price')