from django.shortcuts import render
from .models import *
from inspections.models import *
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import *
from datetime import datetime
import json
import os,uuid

BASE_URL = "https://cloverbuddies.sgp1.digitaloceanspaces.com/cloverbuddies/media/"

class loginView(APIView):
    def post(self,request):
        response = {}
        username = request.data['username']
        password = request.data['password']
        if username == None or password == None:
            print("username or password is null")
            return Response({
                'status':'fail',
                'message':'NoneType Username or Password'
            }, status=403)
        try:
            user = User.objects.get(username=username)
        except Exception as error:
            print(error)
            return Response({
                'status':'fail',
                'message':'Bad Data Encountered',
                'error' : str(error)
            }, status=403)
        if(check_password(password,user.password)):
            if(user.role == 'spcb_user'):
                userState = SPCB.objects.filter(user=user).first()
                if(userState == None):
                    return Response({
                        'status':'fail',
                        'message':'User Not Registered'
                    }, status=403)
                else:
                    response['state'] = userState.state.name
                    response['state_shortName'] = userState.state.short_name
            response['token'] = user.token
            response['role'] = user.role
            response['user'] = username
            response['success'] = 'true'
            return Response(response,status=200)
        else:
            print("no password match")
            response['status'] = 'fail'
            return Response("Invalid username or password",status=403)

class TestView(APIView):
    def get(self,request):
        return Response({'message' : 'app online : )'})
    
class ActiveInspectionsView(APIView):
    def post(self,request):
        response = []
        # print("GET under mystatus")
        tok = request.headers['Authorization']
        print(tok)
        if tok == None:
            return Response({
                'status':'fail',
                'message':'Authentication Failed.'
            }, status=403)
        
        try:
            u = User.objects.get(token = tok)
            institute = Institute.objects.get(user = u)
            inspections = Inspection.objects.filter(assigned_to = institute)
            for inspection in inspections:
                new_inspection = {}
                new_inspection["_id"] = inspection.id
                # print("status : ", inspection.status)
                new_inspection["status"] = inspection.status
                new_inspection["factory"] = {
                    "unitcode" : inspection.factory.unitcode,
                    "name" : inspection.factory.name
                }
                response.append(new_inspection)
            print(len(inspections))
            # print(response)
            return Response(response, status=200)
            
        except Exception as error:
            print(error)
            return Response({
                'status':'fail',
                'message':'Database Error : Error while fetching data.',
                'error' : str(error)
            }, status=403)
        # return Response({'message' : 'app online : )'})
        
class MyAllInspectionsAsView(APIView):
    def post(self,request):
        response = []
        # print("GET under mystatus")
        tok = request.headers['Authorization']
        print(tok)
        if tok == None:
            return Response({
                'status':'fail',
                'message':'Authentication Failed.'
            }, status=403)
        
        try:
            u = User.objects.get(token = tok)
            institute = Institute.objects.get(user = u)
            inspections = Inspection.objects.filter(assigned_to = institute)

            factory_fields = ['name','sector','unitcode','state','district','region','basin','status'];

            for inspection in inspections:
                new_inspection = {}
                new_inspection["_id"] = inspection.id
                new_inspection["factory"] = {}
                
                new_inspection["factory"]["name"] = inspection.factory.name
                new_inspection["factory"]["sector"] = {
                    "name" : inspection.factory.sector.name
                }
                new_inspection["factory"]["unitcode"] = inspection.factory.unitcode
                new_inspection["factory"]["state"] = {
                    "short_name" : inspection.factory.state.short_name,
                    "name" : inspection.factory.state.name
                }
                new_inspection["factory"]["district"] = {
                    "short_code" : inspection.factory.district.short_code, 
                    "name" : inspection.factory.district.name,
                    "state" : {
                        "short_name" : inspection.factory.state.short_name,
                        "name" : inspection.factory.state.name
                    }
                }
                new_inspection["factory"]["basin"] = {
                    "name" : inspection.factory.basin.name
                }
                new_inspection["factory"]["status"] = inspection.factory.status
                new_inspection["status"] = inspection.status
                response.append(new_inspection)
                
            # print(len(inspections))
            # print(response)
            return Response(response, status=200)
            
        except Exception as error:
            print(error)
            return Response({
                'status':'fail',
                'message':'Database Error : Error while fetching data.',
                'error' : str(error)
            }, status=403)
        # return Response({'message' : 'app online : )'})
        
class ConsentCopyUploadView(APIView):
    def post(self, request):
        _id = int(request.data.getlist('inspectionId')[0])
        images = request.data.getlist('consentcopy')[0]
        inspection = Inspection.objects.get(id = _id)
        inspection_report = Inspection_report.objects.create(file = images , inspection = inspection , file_category = "consent_copy")
        return Response({
            "fileLocation" : BASE_URL + str(inspection_report.file)
        })

class InspectionReportUploadView(APIView):
    def post(self, request):
        _id = int(request.data.getlist('inspectionId')[0])
        images = request.data.getlist('inspectionreport')[0]
        inspection = Inspection.objects.get(id = _id)
        inspection_report = Inspection_report.objects.create(file = images , inspection = inspection , file_category = "inspection_report")
        return Response({
            "fileLocation" : BASE_URL + str(inspection_report.file)
        })
        
class AirConsentUploadAsView(APIView):
    def post(self, request):
        _id = int(request.data.getlist('inspectionId')[0])
        images = request.data.getlist('airconsent')[0]
        inspection = Inspection.objects.get(id = _id)
        inspection_report = Inspection_report.objects.create(file = images , inspection = inspection , file_category = "air_consent")
        return Response({
            "fileLocation" : BASE_URL + str(inspection_report.file)
        })
        
class WaterConsentUploadView(APIView):
    def post(self, request):
        _id = int(request.data.getlist('inspectionId')[0])
        images = request.data.getlist('waterconsent')[0]
        inspection = Inspection.objects.get(id = _id)
        inspection_report = Inspection_report.objects.create(file = images , inspection = inspection , file_category = "water_consent")
        return Response({
            "fileLocation" : BASE_URL + str(inspection_report.file)
        })
        
class cgwaNocConsentUploadAsView(APIView):
    def post(self, request):
        _id = int(request.data.getlist('inspectionId')[0])
        images = request.data.getlist('cgwaNoc')[0]
        inspection = Inspection.objects.get(id = _id)
        inspection_report = Inspection_report.objects.create(file = images , inspection = inspection , file_category = "cgwa_noc")
        return Response({
            "fileLocation" : BASE_URL + str(inspection_report.file)
        })
        
class HazardousConsentUploadAsView(APIView):
    def post(self, request):
        _id = int(request.data.getlist('inspectionId')[0])
        images = request.data.getlist('hazardousconsent')[0]
        inspection = Inspection.objects.get(id = _id)
        inspection_report = Inspection_report.objects.create(file = images , inspection = inspection , file_category = "hazardous_consent")
        return Response({
            "fileLocation" : BASE_URL + str(inspection_report.file)
        })

class FinalReportUploadAsView(APIView):
    def put(self,request):
        
        # {
        #     "status":2,
        #     "teamNames":"",
        #     "finalRecommendation":"",
        #     "complianceStatus":1,
        #     "wasteWaterGeneration":"",
        #     "wasteWaterDischarge":"",
        #     "bod":"",
        #     "bodLoad":"",
        #     "cod":"",
        #     "codLoad":"",
        #     "otherChars":"",
        #     "nonInstallationofOCEMS":false,
        #     "temperedOCEMS":false,
        #     "dissentBypassArrangement":false,
        #     "provision":false,
        #     "defunctETP":false,
        #     "":false,
        #     "standardExceedance":false,
        #     "dilutionInETP":false,
        #     "dissentWaterDischarge":false,
        #     "unauthorizedDisposal":false,
        #     "effluent":false,
        #     "invalidCTO":false,
        #     "inspectionDate":"Invalid Date",
        #     "inspectionReportUploadDate":"Tue Dec 21 2021 16:04:39 GMT+0530 (India Standard Time)"
        # }
        
        # model
        #  = models.CharField(max_length=20)
        #  = models.CharField(max_length=20)
        #  = models.CharField(max_length=20)
        #  = models.CharField(max_length=20)
        #  = models.CharField(max_length=20)
        #  = models.IntegerField()
        #  = models.BooleanField()
        #  = models.BooleanField()
        #  = models.BooleanField()
        #  = models.BooleanField()
        #  = models.BooleanField()
        #  = models.CharField(max_length=20)
        #  = models.ForeignKey(Inspection, on_delete=models.CASCADE)
        print(request)
        print(request.data)
        
        inspection = Inspection.objects.get(id = request.data['inspectionId'])
        inspection.status = 2
        inspection.save()
        
        new_inspection_data = Inspection_report_data.objects.create(
            teamNames = request.data['teamNames'],
            wasteWaterGeneration = request.data['wasteWaterGeneration'],
            wasteWaterDischarge = request.data['wasteWaterDischarge'],
            otherChars = request.data['otherChars'],
            nonInstallationofOCEMS = request.data['nonInstallationofOCEMS'],
            temperedOCEMS = request.data['temperedOCEMS'],
            provision = request.data['provision'],
            standardExceedance = request.data['standardExceedance'],
            unauthorizedDisposal = request.data['unauthorizedDisposal'],
            invalidCTO = request.data['invalidCTO'],
            
            ZLDnorms = request.data['ZLDnorms'],
            bod = request.data['bod'],
            bodLoad = request.data['bodLoad'],
            cod = request.data['cod'],
            codLoad = request.data['codLoad'],
            complianceStatus = request.data['complianceStatus'],
            defunctETP = request.data['defunctETP'],
            dilutionInETP = request.data['dilutionInETP'],
            dissentBypassArrangement = request.data['dissentBypassArrangement'],
            dissentWaterDischarge = request.data['dissentWaterDischarge'],
            effluent = request.data['effluent'],
            finalRecommendation = request.data['finalRecommendation'],
            inspection = inspection
        )
        
        return Response({}, status = 200)
    
class GetFieldReportView(APIView):
    def get(self,request):
        inspectionId = request.GET.get('inspectionId')
        
        inspection = Inspection.objects.get(id = inspectionId)
        
        try:
            field_report = Field_report.objects.filter(inspection = inspection)
            field_report = field_report[0]
        except Exception as error:
            print("no report babe : ",error)
            return Response({}, status=403)
        
        factory = Factories.objects.get(inspection = inspection)
        poc = Field_report_poc.objects.filter(field_report = field_report)
        poc = poc[0]
        attendance = Attendance.objects.filter(inspection = inspection)
        attendance = attendance[0]
        images = Field_report_images.objects.filter(field_report = field_report)
        
        imgs = []
        for image in images:
            imgs.append(BASE_URL + str(image.image))
            
        print("imagessssssssssssssssssss : ", imgs)
        
        print("poc : ", poc)
        
        print(field_report)
        
        response = {}
        response['updatedAt'] = field_report.updatedon
        response['factory'] = {
            "name" : factory.name,
            "unitcode" : factory.unitcode,
            "sector" : {
                "name" : factory.sector.name,
            },
        }
        response["attendance"] = {
            "entrylocation" : {
                "lat" : str(attendance.lat),
                "long" : str(attendance.long),
            },
        }
        response["fieldReport"] = {
                "poc" : {
                    "name" : poc.name,
                    "number" : poc.number,
                    "email" : poc.email,
                },
                "uos" : field_report.uos,
                "uosdetail" : field_report.uosdetail,
                "etpos" : field_report.etpos,
                "etposdetail" : field_report.etposdetail,
                "cpc" :field_report.cpc,
                "ipc" : field_report.ipc,
                "ppopd" : field_report.ppopd,
                "fwwpdbofm" : field_report.fwwpdbofm,
                "ocs" : field_report.ocs,
                "sonfc" : field_report.sonfc,
                "mrr" : field_report.mrr,
                "mrrname" : field_report.mrrname,
                "csac" : field_report.csac,
                "wc" : field_report.wc,
                "hc" : field_report.hc,
                "cc" : field_report.cc,
                "sfwc" : field_report.sfwc,
                "sfwcdetail" : field_report.sfwcdetail,
                "fib" : field_report.fib,
                "fibdetail" : field_report.fibdetail,
                "fietpinlet" : field_report.fietpinlet,
                "fietpinletdetail" : field_report.fietpinletdetail,
                "fietpoutlent"  : field_report.fietpoutlent,
                "fietpoutlentdetail" : field_report.fietpoutlentdetail,
                "fmetpoutletcdf" : field_report.fmetpoutletcdf,
                "fmetpoutletpdf" : field_report.fmetpoutletpdf,
                "os" : field_report.os,
                "osdetail" : field_report.osdetail,
                "semfetp" : field_report.semfetp,
                "semfer" : field_report.semfer,
                "specificobservations" : field_report.specificobservations,
                "images" : imgs
            }
        response['status'] = inspection.status
        
        return Response(response)

class GetAllInspectionStateBoard(APIView):
    def get(self,request):
        response = []
        # print("GET under mystatus")
        tok = request.headers['Authorization']
        print(tok)
        if tok == None:
            return Response({
                'status':'fail',
                'message':'Authentication Failed.'
            }, status=403)
        
        try:
            u = User.objects.get(token = tok)
            non_zero_action_data_debug_dict = []

            inspections = Inspection.objects.all()

            factory_fields = ['name','sector','unitcode','state','district','region','basin','status'];

            for inspection in inspections:
                new_inspection = {}
                
                # field_report = Field_report.objects.filter(inspection = inspection)
                # filed_report = field_report[0]
                new_inspection["inspectionDate"] = ""
                new_inspection["inspectionReportUploadDate"] = ""
                
                try:
                    inspection_report = Inspection_report_data.objects.filter(inspection = inspection).first()
                    if(inspection_report != None):
                        new_inspection["inspectionReportUploadDate"] = inspection_report.updatedon
                    #print(dir(inspection_report))
                except Exception as error:
                    # print(error)
                    pass
                
                try:
                    attendance = Attendance.objects.filter(inspection = inspection).first()
                    if(attendance != None):
                        new_inspection["inspectionDate"] = attendance.updatedon
                except Exception as error:
                    # print(error)
                    pass
                    
                # print("Inspection Report : ", inspection_report.first())
                # inspection_report = inspection_report.first()
                new_inspection["_id"] = inspection.id
                
                new_inspection["factory"] = {}
                
                new_inspection["factory"]["name"] = inspection.factory.name
                new_inspection["factory"]["sector"] = {
                    "name" : inspection.factory.sector.name
                }
                new_inspection["factory"]["unitcode"] = inspection.factory.unitcode
                new_inspection["factory"]["state"] = {
                    "short_name" : inspection.factory.state.short_name,
                    "name" : inspection.factory.state.name
                }
                new_inspection["factory"]["district"] = {
                    "short_code" : inspection.factory.district.short_code, 
                    "name" : inspection.factory.district.name,
                    "state" : {
                        "short_name" : inspection.factory.state.short_name,
                        "name" : inspection.factory.state.name
                    }
                }
                new_inspection["factory"]["basin"] = {
                    "name" : inspection.factory.basin.name.lower()
                }
                try:
                    action_data = Action_report.objects.filter(inspection = inspection)
                except Exception as error:
                    action_data = []
                    
                non_zero_action_data_debug_dict.append(str(inspection))
                
                new_inspection["actions"] = []
                for action in action_data:
                    print("action : ", action, action.compliance_status)
                    new_inspection["actions"].append({
                        "complianceStatus" : action.compliance_status,
                        "showcausenoticeStatus" : action.showcausenoticestatus
                    })
                new_inspection["factory"]["status"] = inspection.factory.status
                new_inspection["status"] = inspection.status
                new_inspection["assignedTo"] = {
                    "username" : inspection.assigned_to.institute
                }
                response.append(new_inspection)
                
            # print(len(inspections))
            print("action non zero data : ", non_zero_action_data_debug_dict)
            print(response)
            return Response(response, status=200)
            
        except Exception as error:
            print(error)
            print("aaaaaaaaaa : " , error)
            return Response({
                'status':'fail',
                'message':'Database Error : Error while fetching data.',
                'error' : str(error)
            }, status=403)
        # return Response({'message' : 'app online : )'})
        
class GetInspectionReportView(APIView):
    def get(self,request):
        try:
            id = request.GET.get('id')
            inspection = Inspection.objects.get(id = id)
            print("inspection : ", inspection)
            attendance = Attendance.objects.filter(inspection = inspection).first()
            response = {}

            response["inspectionDate"] = attendance.updatedon
            response["factory"] = {
                "name" : inspection.factory.name
            }
            response["status"] = inspection.status
            
            inspection_report_data = Inspection_report_data.objects.filter(inspection = inspection).first()
            response["teamNames"] = inspection_report_data.teamNames
            
            response["finalRecommendation"] = inspection_report_data.finalRecommendation;
            response["complianceStatus"] = inspection_report_data.complianceStatus

            try:
                action_data = Action_report.objects.filter(inspection = inspection)
            except Exception as error:
                action_data = []
                    
            # dummy data
            response["actions"] = []   
            action_report_files = Action_report_files.objects.filter(inspection = inspection)
            action_report_files = [str(files.file) for files in action_report_files if str(files.file).strip() != '']
            
            if len(action_report_files) > 0:
                print("Action Report Files" , action_report_files)
            
            for action in action_data:
                print("action : ", action, action.compliance_status)
                response["actions"].append({
                    "complianceStatus" : action.compliance_status,
                    "showcausenoticeStatus" : action.showcausenoticestatus,
                    "date" : action.updated_at,
                    "finalRecommendation" : action.finalrecommendation,
                    "reports" : action_report_files
                })
            response["report"] = {
                "files" : []
            }
            
            inspection_image_files = Inspection_report.objects.filter(inspection = inspection)
            for image in inspection_image_files:
                response["report"]["files"].append(str(image.file))
                
            response["factory"]["sector"] = {}
            response["factory"]["sector"] = {
                "name" : inspection.factory.sector.name
            }
            
            field_report = Field_report.objects.filter(inspection = inspection).first()
            print("field_report : " , field_report)
            field_report_poc = Field_report_poc.objects.filter(field_report = field_report).first()
            print("poc : ", field_report_poc)
            
            response["fieldReport"] = {
                "poc" : {
                    "name" : field_report_poc.name, 
                    "number" : field_report_poc.number,
                    "email" : field_report_poc.email
                }
            }
            
            print(response)
            return Response(response, 200)
        except Exception as error:
            print(error)
            return Response({}, 500)
        
class MyCompletedInspectionsAsView(APIView):
    def get(self,request):
        response = []
        # print("GET under mystatus")
        tok = request.headers['Authorization']
        print(tok)
        if tok == None:
            return Response({
                'status':'fail',
                'message':'Authentication Failed.'
            }, status=403)
        
        try:
            u = User.objects.get(token = tok)

            inspections = Inspection.objects.all()

            factory_fields = ['name','sector','unitcode','state','district','region','basin','status'];
            print(inspections)
            
            d = {}
            d[0] = 0
            d[1] = 0
            d[2] = 0
            d[3] = 0
            d[4] = 0
            d[5] = 0

            for inspection in inspections:
                # print(inspection.status)
                d[inspection.status] += 1
                if inspection.status == 0:
                    continue
                
                new_inspection = {}
                
                # field_report = Field_report.objects.filter(inspection = inspection)
                # filed_report = field_report[0]
                new_inspection["inspectionDate"] = ""
                new_inspection["inspectionReportUploadDate"] = ""
                
                try:
                    inspection_report = Inspection_report_data.objects.filter(inspection = inspection).first()
                    if(inspection_report != None):
                        new_inspection["inspectionReportUploadDate"] = inspection_report.updatedon
                    # print(dir(inspection_report))
                except Exception as error:
                    print(error)
                    pass
                
                try:
                    attendance = Attendance.objects.filter(inspection = inspection).first()
                    if(attendance != None):
                        new_inspection["inspectionDate"] = attendance.updatedon
                except Exception as error:
                    print(error)
                    pass
                    
                # print("Inspection Report : ", inspection_report.first())
                # inspection_report = inspection_report.first()
                new_inspection["_id"] = inspection.id
                
                new_inspection["factory"] = {
                    "region" : inspection.factory.region
                }
                
                new_inspection["factory"]["name"] = inspection.factory.name
                new_inspection["factory"]["sector"] = {
                    "name" : inspection.factory.sector.name,
                    "region" : inspection.factory.region
                }
                new_inspection["factory"]["unitcode"] = inspection.factory.unitcode
                new_inspection["factory"]["state"] = {
                    "short_name" : inspection.factory.state.short_name,
                    "name" : inspection.factory.state.name
                }
                new_inspection["factory"]["district"] = {
                    "short_code" : inspection.factory.district.short_code, 
                    "name" : inspection.factory.district.name,
                    "state" : {
                        "short_name" : inspection.factory.state.short_name,
                        "name" : inspection.factory.state.name
                    }
                }
                new_inspection["factory"]["basin"] = {
                    "name" : inspection.factory.basin.name.lower()
                }
                
                try:
                    action_data = Action_report.objects.filter(inspection = inspection)
                except Exception as error:
                    action_data = [""]
                
                # print("action report : ", action_data)
                new_inspection["actions"] = [str(actions.inspection.factory.name) for actions in action_data]
                
                new_inspection["factory"]["status"] = inspection.factory.status
                new_inspection["status"] = inspection.status
                new_inspection["assignedTo"] = {
                    "username" : inspection.assigned_to.institute
                }
                response.append(new_inspection)
                
            # print(len(inspections))
            # print(response)
            print(d)
            return Response(response, status=200)
            
        except Exception as error:
            print(error)
            print("aaaaaaaaaa : " , error)
            return Response({
                'status':'fail',
                'message':'Database Error : Error while fetching data.',
                'error' : str(error)
            }, status=403)
        # return Response({'message' : 'app online : )'})
        
class ActionReportUploadView(APIView):
    def post(self, request):
        _id = int(request.data.getlist('inspectionId')[0])
        print("The id is : ", _id)
        images = request.data.getlist('actionreport')[0]
        inspection = Inspection.objects.get(id = _id)
        inspection_report = Action_report_files.objects.create(file = images , inspection = inspection)
        return Response({
            "fileLocation" : BASE_URL + str(inspection_report.file)
        })
        # return Response({}, 200)
        
class InspectionActionSubmitView(APIView):
    def post(self, request):
        tok = request.headers['Authorization']
        print(tok)
        if tok == None:
            return Response({
                'status':'fail',
                'message':'Authentication Failed.'
            }, status=403)
        
        print("putttttttttttttttttttttttttttttttttttttt")
        print(request.data)
        print("request data : ", request.data['inspectionId'])
        _id = int(request.data['inspectionId'])
        u = User.objects.get(token = tok)
        inspection = Inspection.objects.get(id = _id)
        request.data["date"] = request.data["date"].replace('(India Standard Time)', '').rstrip()
        datetime_object = datetime.strptime(request.data["date"], '%a %b %d %Y %H:%M:%S %Z%z').strftime("%Y-%m-%d %H:%M:%S")
        print(datetime_object)
        action_report = Action_report.objects.create(
            compliance_status = request.data["complianceStatus"],
            showcausenoticestatus = request.data["showcausenoticeStatus"],
            date = datetime_object,
            finalrecommendation = request.data["finalRecommendation"],
            inspection = inspection,
            created_by = u
        )
        return Response({} , 200)