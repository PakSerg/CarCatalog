from rest_framework import serializers
from .models import Car
from datetime import datetime


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

    def validate_year(self, value):
        if value < 1886 or value > datetime.now().year:
            raise serializers.ValidationError('Invalid year of release')
        return value 