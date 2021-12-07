
from django.urls import path,include
from .views import *

urlpatterns = [
    path('auth/login',loginView.as_view(),name='login'),
]