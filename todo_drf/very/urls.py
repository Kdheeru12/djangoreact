from django.urls import path
from .views  import *

urlpatterns = [
    path('',BlogList.as_view(),name='hello' ),
    path('<int:pk>',BlogDetail.as_view(),name='detail'),
    path('api/reg',Register.as_view(),name='register')
]