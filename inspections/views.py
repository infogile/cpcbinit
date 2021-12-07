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
            print(response)
            return Response(response,status=200)
        else:
            response['status'] = 'fail'
            return Response("Invalid username or password",status=403)
    