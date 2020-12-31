from django.urls import path
from rest_framework import urlpatterns
from .views  import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('',BlogList,basename='blog')
urlpatterns = router.urls

# urlpatterns = [
#     path('',BlogList.as_view({'get': 'list'}),name='hello' ),
#     # path('<int:pk>',BlogDetail.as_view(),name='detail'),
#     # path('api/reg',Register.as_view(),name='register'),
#     # path('api/logout',BlacklistTokens.as_view(),name='blacklist')

# ]