from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from decimal import Decimal


class Car(models.Model): 

    class FuelType(models.TextChoices):
        PETROL = 'бензин', 'бензин'
        DIESEL = 'дизель', 'дизель'
        ELECTRIC = 'электричество', 'электричество'
        HYBRID = 'гибрид', 'гибрид'

    class Transmission(models.TextChoices):
        MANUAL = 'механическая', 'механическая'
        AUTOMATIC = 'автоматическая', 'автоматическая'
        CVT = 'вариатор', 'вариатор'
        DCT  = 'робот', 'робот'

    brand = models.CharField(max_length=50, null=False) 
    model  = models.CharField(max_length=100, null=False) 
    year = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1886, 'The year of release cannot be less than 1886'),
        MaxValueValidator(datetime.now().year, 'The year of release cannot be more than the current year')
    ])
    fuel_type = models.CharField(max_length=13, choices=FuelType.choices, null=False)
    transmission = models.CharField(max_length=14, choices=Transmission.choices, null=False)
    mileage = models.PositiveIntegerField(null=False)
    price = models.DecimalField(null=False, max_digits=10, decimal_places=2, validators=[
            MinValueValidator(Decimal('0.00'), 'The price cannot be negative')
        ])

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"