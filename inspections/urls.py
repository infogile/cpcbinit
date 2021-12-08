
from django.urls import path,include
from .views import *

urlpatterns = [
    path('auth/login',loginView.as_view(),name='login'),
    path('inspection/mystatus',mystatusView.as_view(),name='mystatus'),
    path('inspection/myinspection',myinspectionView.as_view(),name='myinspection'),
    path('inspection/myfieldReport',myfieldReportView.as_view(),name='myfieldReport'),
]