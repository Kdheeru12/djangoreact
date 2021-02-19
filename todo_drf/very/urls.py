from django.urls import path
from rest_framework import urlpatterns
from .views  import *
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# # router.register('',BlogList,basename='blog')
# router.register('shop',GroceriesList,basename='shop')
# urlpatterns = router.urls

urlpatterns = [
    path('',GroceriesList.as_view(),name='hello' ),
    #path('<slug:pk>/',BlogDetail.as_view(),name='detail'),
    # path('search/',ProductList.as_view(),name='prod')
]