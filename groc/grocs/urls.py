from django.urls import path
from rest_framework import urlpatterns
from .views  import *


urlpatterns = [
    path('',GroceriesList.as_view(),name='hello' ),
]