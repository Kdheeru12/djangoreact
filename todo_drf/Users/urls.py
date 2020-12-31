from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('reg',Register.as_view(),name='register'),
    path('logout',BlacklistTokens.as_view(),name='blacklist')
]