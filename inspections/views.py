from django.shortcuts import render
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import *
import json
import os,uuid

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
            response['token'] = user.token
            response['role'] = user.role
            response['success'] = 'true'
            return Response(response,status=200)
        else:
            print("no password match")
            response['status'] = 'fail'
            return Response("Invalid username or password",status=403)
        
class mystatusView(APIView):
    def get(self, request):
        response = {}
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
            inspection_status = my_status.objects.filter(institute =institute).first()
            if(inspection_status == None):
                inspection_status = my_status(institute = institute)
                inspection_status.save()
            total_assigned = inspection_status.total_assigned
            total_inspected = inspection_status.total_inspected
            total_closed = inspection_status.total_factory_closed
            bypass = inspection_status.bypass
        except Exception as error:
            print(error)
            return Response({
                'status':'fail',
                'message':'Database Error : Error while fetching data.',
                'error' : str(error)
            }, status=403)
            

        # for inspection in institute_inspections:
        #     if inspection.status == 0:
        #         total_assigned += 1
        #     elif inspection.status == 1:
        #         total_inspected += 1
        #     if inspection.factory.status == 4:
        #         total_closed += 1

        # STATUS CODES 
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
                'totalBypass':bypass
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
        
        # print("POST")
        # print(request.headers)
        # print(request.data)
        
        try:
            tok = request.headers['Authorization']
            u = User.objects.get(token = tok)
            institute = Institute.objects.get(user = u)
            institute_inspections = Inspection.objects.filter(assigned_to = institute)
        except Exception as error:
            print(error)
            return Response({
                'status':'fail',
                'message':'Database Error : Error occured while fetching',
                'error' : str(error)
            }, status=403)

        response = []
        if institute_inspections == None or institute_inspections == []:
            return Response({
                'success':'true',
            }, status=403)
        for inspection in institute_inspections:
            if inspection.status == 0:
                temp = {}
                temp['success'] = 'true'
                temp["_id"] = inspection.id
                temp["factory"] = {
                        "location": {
                            "coordinates": []
                        },
                        "_id": inspection.id,
                        "name": ", ".join([str(inspection.factory.name), str(inspection.factory.region), str(inspection.factory.district), str(inspection.factory.state)]),
                        "sector": {
                            "_id": inspection.factory.sector.id,
                            "name": inspection.factory.sector.name
                        },
                        "unitcode": inspection.factory.unitcode,
                        "state": {
                            "_id": inspection.factory.state.id,
                            "name": inspection.factory.state.name
                        },
                        "district": {
                            "_id": inspection.factory.district.id,
                            "name": inspection.factory.district.name
                        },
                        "region": inspection.factory.region,
                        "basin": {
                            "_id": inspection.factory.basin.id,
                            "name": inspection.factory.basin.name
                        }
                }
                try:
                    response.append(temp)
                except Exception as error:
                    print(error)
                    return Response({
                        'status':'fail',
                        'message':'No relevant data found.'
                    }, status=403)
            
        return Response(response,status=200)



class myfieldReportView(APIView):
    def post(self, request, *args, **kwargs):
        response = {}

        
        tok = request.headers['Authorization']
        if tok == None:
            return Response({
                'status':'fail',
                'message':'NoneType Data Encountered'
            }, status=403)
        
        try:
            u = User.objects.get(token = tok)
            institute = Institute.objects.get(user = u)
        except Exception as error:
            print(error)
            return Response({
                'status':'fail',
                'message':'Database error : Error occured while fetching',
                'error' : str(error)
            }, status=403)
        
        
        print("POST")
        print(request.headers)
        print('bhaiya maze',request.data)
        print('bhaiya maze',type(request.data['body']))
        print('bhaiya maze',request.data['body'])

        try:
            dat = json.loads(request.data['body'])
        except Exception as error:
            print(error)
            return Response({
                'status':'fail',
                'message':'Bad Data Encountered',
                'error':str(error)
            }, status=403)
        
        ######### parsing #########
        id_ = dat["id"]
        _attendance = dat["attendance"]
        _entrylocation = _attendance["entrylocation"]
        _type = _entrylocation["type"]
        _coordinates = _entrylocation["coordinates"]
        _fieldReport = dat["fieldReport"]
        # _images = _fieldReport["images"]    # maybe not required
        try:
            _poc = _fieldReport["poc"][0]
            print(_poc)
        except Exception as error:
            print(error)
        _fieldReportPOC = {}
        ks_poc = ["name","number","email"]
        for def_key in ks_poc:
            if(def_key == "number"):
                _fieldReportPOC.setdefault(def_key,0)
            elif(def_key == "email"):
                _fieldReportPOC.setdefault(def_key,"null@null.null")
            else:
                _fieldReportPOC.setdefault(def_key,"NA")
        try:
            _fieldReportPOC["name"] = _poc["name"]
        except Exception as error:
            print(error)
        try:    
            _fieldReportPOC["number"] = _poc["email"] #code sahi hai frontend mai email mai no aa raha hai
        except Exception as error:
            print(error)
        try:
            _fieldReportPOC["email"] = _poc["number"] #code sahi hai frontend mai number mai email aa raha hai
        except Exception as error:
            print(error)
        
        # _uos = _fieldReport["uos"]
        # _uosdetail = _fieldReport["uosdetail"]
        # _etpos = _fieldReport["etpos"]
        # _etposdetail = _fieldReport["etposdetail"]
        # _cpc = _fieldReport["cpc"]
        # _ipc = _fieldReport["ipc"]
        # _ppopd = _fieldReport["ppopd"]
        # _fwwpdbofm = _fieldReport["fwwpdbofm"]
        # _ocs = _fieldReport["ocs"]
        # _sonfc = _fieldReport["sonfc"]
        # _mrr = _fieldReport["mrr"]
        # _mrrname = _fieldReport["mrrname"]
        # _csac = _fieldReport["csac"]
        # _wc = _fieldReport["wc"]
        # _hc = _fieldReport["hc"]
        # _cc = _fieldReport["cc"]
        # _sfwc = _fieldReport["sfwc"]
        # _sfwcdetail = _fieldReport["sfwcdetail"]
        # _fib = _fieldReport["fib"]
        # _fibdetail = _fieldReport["fibdetail"]
        # _fietpinlet = _fieldReport["fietpinlet"]
        # _fietpinletdetail = _fieldReport["fietpinletdetail"]
        # _fietpoutlent  = _fieldReport["fietpoutlent"]
        # _fietpoutlentdetail = _fieldReport["fietpoutlentdetail"]
        # _fmetpoutletcdf = _fieldReport["fmetpoutletcdf"]
        # _fmetpoutletpdf = _fieldReport["fmetpoutletpdf"]
        # _os = _fieldReport["os"]
        # _osdetail = _fieldReport["osdetail"]
        # _semfetp = _fieldReport["semfetp"]
        # _semfer = _fieldReport["semfer"]
        # _specificobservations = _fieldReport["specificobservations"]
        
        try:
            inspection_id = dat['id']
            # inspection = Inspection.objects.filter(id=inspection_id).first()
            # inspection_status = my_status.objects.get(institute = institute)
            # inspection_status.total_inspected += 1
            # inspection.status = 1
            # inspection_status.save()
            # inspection.save()
            inspection_2 = Inspection.objects.get(id=inspection_id)
            print(inspection_2,"inspection 2 yoooooooooooooo")
        except Exception as error:
            print(error)
            return Response({
                'status':'fail',
                'message':'Updation Error : Error while saving Inspection Instance',
                'error' : str(error)
            }, status=403)
        try:
            if(_coordinates[0] == 'loading' or _coordinates[1] == 'loading'):
                _coordinates[0] = 0
                _coordinates[1] = 0

            attendance_instance = Attendance.objects.create(lat = _coordinates[0], long = _coordinates[1], inspection = inspection_2)
        except Exception as error:
            print(error)
            return Response({
                'status':'fail',
                'message':'Creation Error : Error while saving Attendance Instance',
                'error' : str(error)
            }, status=403)
        
        try:
            ks = ["uos" ,"uosdetail" ,"etpos",
            "etposdetail" ,"cpc" ,
            "ipc" ,"ppopd", "fwwpdbofm" ,
            "ocs", "sonfc" ,"mrr" ,
            "mrrname" ,"csac" ,
            "wc" ,"hc" ,"cc" ,
            "sfwc" ,"sfwcdetail" ,
            "fib" ,"fibdetail" ,"fietpinlet" ,
            "fietpinletdetail" ,"fietpoutlent", 
            "fietpoutlentdetail" ,"fmetpoutletcdf" ,
            "fmetpoutletpdf" ,"os", 
            "osdetail" ,"semfetp" ,"semfer" ,"specificobservations"
            ]
            for default_keys in ks:
                _fieldReport.setdefault(default_keys,"N/A")
            
            print(type(_fieldReport))
            print(_fieldReport,'fieldreport after key additionaaaaaaaaaaaaaa')

            fieldReport = Field_report.objects.create(
                uos = _fieldReport["uos"],
                uosdetail = _fieldReport["uosdetail"],
                etpos = _fieldReport["etpos"],
                etposdetail = _fieldReport["etposdetail"],
                cpc = _fieldReport["cpc"],
                ipc = _fieldReport["ipc"],
                ppopd = _fieldReport["ppopd"],
                fwwpdbofm = _fieldReport["fwwpdbofm"],
                ocs = _fieldReport["ocs"],
                sonfc = _fieldReport["sonfc"],
                mrr = _fieldReport["mrr"],
                mrrname = _fieldReport["mrrname"],
                csac = _fieldReport["csac"],
                wc = _fieldReport["wc"],
                hc = _fieldReport["hc"],
                cc = _fieldReport["cc"],
                sfwc = _fieldReport["sfwc"],
                sfwcdetail = _fieldReport["sfwcdetail"],
                fib = _fieldReport["fib"],
                fibdetail = _fieldReport["fibdetail"],
                fietpinlet = _fieldReport["fietpinlet"],
                fietpinletdetail = _fieldReport["fietpinletdetail"],
                fietpoutlent  = _fieldReport["fietpoutlent"],
                fietpoutlentdetail = _fieldReport["fietpoutlentdetail"],
                fmetpoutletcdf = _fieldReport["fmetpoutletcdf"],
                fmetpoutletpdf = _fieldReport["fmetpoutletpdf"],
                os = _fieldReport["os"],
                osdetail = _fieldReport["osdetail"],
                semfetp = _fieldReport["semfetp"],
                semfer = _fieldReport["semfer"],
                specificobservations = _fieldReport["specificobservations"],
                inspection = inspection_2
            )    

        except Exception as error:
            print(error,error.__class__)
            return Response({
                'status':'fail',
                'message':'Object Creation Error : Field Report Instance could not be created',
                'error' : str(error)
            }, status=403)

        try:
            field_report_pos = Field_report_poc.objects.create(
                name = _fieldReportPOC["name"],
                number = _fieldReportPOC["number"],
                email = _fieldReportPOC["email"],
                field_report = fieldReport
            )
        except Exception as error:
            print(error)
        # fieldReport.save()

        try:
            datae = request.data
            image = datae.getlist('images')
            print(request.data['images'])
            # image = request.data['images'] #array of images
            print(type(image))
            print(inspection_2,"aaaaaaaaaaaaaaaaaaaaaaaaaa")
            field_report = Field_report.objects.filter(inspection=inspection_2).first()
            print('field report',field_report)
        except Exception as error:
            print(error)
            return Response({
                'status':'fail',
                'message':'Database Error : Error occured while fetching.',
                'error' : str(error)
            }, status=403)
        if(field_report == None):
            pass
        else:
            try:
                # for img in image:
                print(image)
                if(type(image) == list):
                    for img in image:    
                        img_field = Field_report_images.objects.create(image = img, field_report = field_report)
                else:
                    img_field = Field_report_images.objects.create(image = image, field_report = field_report)
            except Exception as error:
                print(error)
                return Response({
                'status':'fail',
                'message':'Image Upload Error : Failed to upload image(s).',
                'error' : str(error)
            }, status=403)
        try:
            inspection_status = my_status.objects.get(institute = institute)
            if(Field_report.objects.filter(inspection=inspection_2).count() == 1):
                inspection_status.total_inspected += 1
            if(field_report.uos == 'non-operational'):
                inspection_status.total_factory_closed += 1
            inspection_2.status = 1
            inspection_status.save()
            inspection_2.save()
            factory = Factories.objects.filter(id = inspection_2.factory.id).first()
            if(field_report.uos == 'non-operational'):
                factory.status = 4
            else:
                factory.status = 1
            factory.save()
        except Exception as error:
            print('error at end',error)
            return Response({
                'status':'fail',
                'message':'Database Error : Error occured while fetching.',
                'error' : str(error)
            }, status=502)

        response = {
            'payload':{
                'success':'true',
            }
        }
        return Response(response,status=200)
    
    def get(self, request):
        return Response("cool",status=200)
        

    