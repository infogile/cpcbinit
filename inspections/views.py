from django.shortcuts import render
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import *
import json
import os,uuid
# Create your views here.


class loginView(APIView):
    def post(self,request):
        response = {}
        username = request.data['username']
        password = request.data['password']
        user = User.objects.get(username=username)
        if(check_password(password,user.password)):
            response['token'] = user.token
            response['success'] = 'true'
            return Response(response,status=200)
        else:
            response['status'] = 'fail'
            return Response("Invalid username or password",status=403)


class mystatusView(APIView):
    def get(self, request):
        response = {}
        print("GET under mystatus")
        tok = request.data['token']
        u = User.objects.get(token = tok)
        institute = Institute.objects.get(user = u)
        institute_inspections = Inspection.objects.filter(assigned_to = institute)
   
        total_assigned = 0
        total_inspected = 0
        total_closed = 0

        for inspection in institute_inspections:
            if inspection.status == 0:
                total_assigned += 1
            elif inspection.status == 1:
                total_inspected += 1
            if inspection.factory.status == 4:
                total_closed += 1

        # totalAssigned : status 0
        # totalInspected : status 1
        # web portal -> upload report => status 2
        # taken action : status 3
        # if factory closed : status 4
        response = {
            'data':{
                'success':'true',
                'totalAssigned': total_assigned,
                'totalInspected': total_inspected,
                'totalClosed': total_closed,
                'totalBypass':'4'
            }
        }

        return Response(response,status=200)

    def post(self, request):
        response = {}
        print("POST")
        print(str(request))
        print(request.data)
        response['success'] = 'true'
        # response['sector'] = 'heavy industry'
        # response['unitcode'] = '1'
        return Response(response,status=200)

class myinspectionView(APIView):
    def get(self, request):
        response = {}
        print("GET")
        print(str(request))
        print(request.data)
        response['success'] = 'true'
        response['sector'] = 'heavy industry'
        response['state'] = 'West Bengal'
        response['district'] = 'Kolkata'
        response['basin'] = 'heavy industry'
        response['unitcode'] = '1'

        return Response(response,status=200)
    def post(self, request):
        response = {}
        print("POST")
        print(request.headers)
        print(request.data)
        response = [{
            'success':'true',
                "_id": "1",
                "factory": {
                    "location": {
                        "coordinates": []
                    },
                    "_id": "1",
                    "name": "N.I.F. PVT LTD (Namastey India Food), VILL-BRAHAMPUR SHIVRAJPUR, KANPUR",
                    "sector": {
                        "_id": "1",
                        "name": "food & beverages"
                    },
                    "unitcode": 357,
                    "state": {
                        "_id": "1",
                        "name": "Uttar Pradesh"
                    },
                    "district": {
                        "_id": "1",
                        "name": "Kanpur Nagar"
                    },
                    "region": "KANPUR NAGAR",
                    "basin": {
                        "_id": "1",
                        "name": "ganga"
                    }
                },
        },{
            'success':'true',
                "_id": "1",
                "factory": {
                    "location": {
                        "coordinates": []
                    },
                    "_id": "1",
                    "name": "N.I.F. PVT LTD (Namastey India Food), VILL-BRAHAMPUR SHIVRAJPUR, KANPUR",
                    "sector": {
                        "_id": "1",
                        "name": "textile"
                    },
                    "unitcode": 357,
                    "state": {
                        "_id": "1",
                        "name": "Uttar Pradesh"
                    },
                    "district": {
                        "_id": "1",
                        "name": "Kanpur Nagar"
                    },
                    "region": "KANPUR NAGAR",
                    "basin": {
                        "_id": "1",
                        "name": "ganga"
                    }
                }
        },{
            'success':'true',
            "_id": "1",
                "factory": {
                    "location": {
                        "coordinates": []
                    },
                    "_id": "1",
                    "name": "Complete",
                    "sector": {
                        "_id": "1",
                        "name": "Nothing left"
                    },
                    "unitcode": 357,
                    "state": {
                        "_id": "1",
                        "name": "Uttar Pradesh"
                    },
                    "district": {
                        "_id": "1",
                        "name": "Kanpur Nagar"
                    },
                    "region": "KANPUR NAGAR",
                    "basin": {
                        "_id": "1",
                        "name": "ganga"
                    }
                }
        }
        ]

        return Response(response,status=200)



class myfieldReportView(APIView):
    def post(self, request, *args, **kwargs):
        response = {}
        print("POST")
        print(request.headers)
        print('bhaiya maze',request.data['body'])
        print('bhaiya maze',type(request.data['body']))
        print('bhaiya maze',request.data['body'])

        dat = json.loads(request.data['body'])

        image = request.data['images'] #array of images
        inspection_id = dat['id']
        inspection = Inspection.objects.get(pk=inspection_id)
        field_report = Field_report.objects.get(pk=inspection_id)
        field_report = Field_report(
            inspection=inspection,
        )
        field_report.save()
        if(inspection == None):
            pass
        else:
            img_field = Field_report_images(image = image,field_report = field_report)
            img_field.save()

        
        response = {
            'payload':{
                'success':'true',
            }
        }
        return Response(response,status=200)
    def get(self, request):
        return Response("cool",status=200)

    