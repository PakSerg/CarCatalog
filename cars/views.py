from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Car
from .serializers import CarSerializer
from .filters import CarFilter
from .services import PaginationCars


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all() 
    serializer_class = CarSerializer 
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]  
    filterset_class = CarFilter  
    pagination_class = PaginationCars
