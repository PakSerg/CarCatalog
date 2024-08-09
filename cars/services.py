from rest_framework.pagination import PageNumberPagination 
from .models import Car 


class PaginationCars(PageNumberPagination): 
    page_size = 5 
    max_page_size = 50

    def paginate_queryset(self, queryset, request, view=None):
        queryset = queryset.order_by('id')  
        return super().paginate_queryset(queryset, request, view)