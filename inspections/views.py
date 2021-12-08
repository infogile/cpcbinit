from django.shortcuts import render
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import *
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
        print(request.data)
        #response['success'] = 'true'
        response = {
            'data':{
                'success':'true',
                'totalAssigned':'10',
                'totalInspected':'5',
                'totalClosed':'0',
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
        # response = {
        #     'data':{
        #         'success':'true',
        #         'factory':{
        #             'unitcode':'1',
        #             'name':'LNT',
        #             'state':{'name':'West Bengal'},
        #             'region':'kolkata area',
        #             'district':{'name':'Kolkata'},
        #             'basin':{'name':'heavy industry'},
        #             'location':{'coordinates':'12.34,56.78'},
        #         }
        #     }
        # }
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
        # response = {
        #     'data':[{
        #         'success':'true',
        #         "_id": "1",
        #         "factory": {
        #             "location": {
        #                 "coordinates": []
        #             },
        #             "_id": "1",
        #             "name": "N.I.F. PVT LTD (Namastey India Food), VILL-BRAHAMPUR SHIVRAJPUR, KANPUR",
        #             "sector": {
        #                 "_id": "1",
        #                 "name": "food & beverages"
        #             },
        #             "unitcode": 357,
        #             "state": {
        #                 "_id": "1",
        #                 "name": "Uttar Pradesh"
        #             },
        #             "district": {
        #                 "_id": "1",
        #                 "name": "Kanpur Nagar"
        #             },
        #             "region": "KANPUR NAGAR",
        #             "basin": {
        #                 "_id": "1",
        #                 "name": "ganga"
        #             }
        #         }
        #     },{
        #             'success':'true',
        #         "_id": "1",
        #         "factory": {
        #             "location": {
        #                 "coordinates": []
        #             },
        #             "_id": "1",
        #             "name": "N.I.F. PVT LTD (Namastey India Food), VILL-BRAHAMPUR SHIVRAJPUR, KANPUR",
        #             "sector": {
        #                 "_id": "1",
        #                 "name": "food & beverages"
        #             },
        #             "unitcode": 357,
        #             "state": {
        #                 "_id": "1",
        #                 "name": "Uttar Pradesh"
        #             },
        #             "district": {
        #                 "_id": "1",
        #                 "name": "Kanpur Nagar"
        #             },
        #             "region": "KANPUR NAGAR",
        #             "basin": {
        #                 "_id": "1",
        #                 "name": "ganga"
        #             }
        #         }
        #     }]
            
        #}

        #response = {'data':{'cool':'cool'}}

        # response['sector'] = 'heavy industry'
        # response['state'] = 'West Bengal'
        # response['district'] = 'Kolkata'
        # response['basin'] = 'heavy industry'
        # response['unitcode'] = '1'

        return Response(response,status=200)



class myfieldReportView(APIView):
    def post(self, request, *args, **kwargs):
        response = {}
        print("POST")
        print(request.headers)
        print('bhaiya maze',request.data)
        response = {
            'payload':{
                'success':'true',
            }
        }
        return Response(response,status=200)
    def get(self, request):
        return Response("cool",status=200)

    