
from django.urls import path,include
from .views import *

urlpatterns = [
    path('test',TestView.as_view(), name='test'),
    path('auth/login',loginView.as_view()),
    path('inspection/myactiveinspection',ActiveInspectionsView.as_view()),
    path('inspection/myallinspection', MyAllInspectionsAsView.as_view()),
    path('inspection/consentcopy', ConsentCopyUploadView.as_view()),
    path('inspection/inspectionreport', InspectionReportUploadView.as_view()),
    path('inspection/airconsent', AirConsentUploadAsView.as_view()),
    path('inspection/waterconsent', WaterConsentUploadView.as_view()),
    path('inspection/cgwaNoc', cgwaNocConsentUploadAsView.as_view()),
    path('inspection/hazardousconsent', HazardousConsentUploadAsView.as_view()),
    path('inspection/finalreportupload', FinalReportUploadAsView.as_view()),
    path('inspection/getfieldreport', GetFieldReportView.as_view()),
    path('inspection/allinspection', GetAllInspectionStateBoard.as_view()),
    path('inspection/getinspectionreport', GetInspectionReportView.as_view())
]