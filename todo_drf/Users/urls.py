from django.urls import path
from . import views
from .views import *
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('logout',BlacklistTokens.as_view(),name='blacklist'),
    path('get_user/',GETUSER.as_view(),name='getUsers')
]


router = DefaultRouter()
router.register('reg',Users,basename='users')

urlpatterns += router.urls

