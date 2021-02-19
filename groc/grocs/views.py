from django.shortcuts import render
from .models import Groceries
from rest_framework import generics
from .searilizers import GroceriesSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

# Create your views here.
class GroceriesList(generics.ListAPIView):
    queryset = Groceries.objects.all()
    serializer_class = GroceriesSerializer
    pagination_class=PageNumberPagination
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['^title','^description']
    filterset_fields = ['price']
    ordering_fields = ['price','created']