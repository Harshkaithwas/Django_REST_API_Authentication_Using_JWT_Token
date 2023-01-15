from django.shortcuts import render

# Create your views here.
from accounts.serializers import *
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken



class RegistrationView(APIView):
    serializer_class = RegistrationSerializer

    def get(self, request):
        return render(request, 'base.html')
    

    def post(self, request, *args, **kwargs):

        serializer = RegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            refresh = RefreshToken.for_user(Account)
            response={
                'message':'Your Account Has Been Registerd Sucessfully',
                'refresh': str(refresh),
                'access': str(refresh.access_token),

            }
            return Response(response, status=status.HTTP_201_CREATED)
    
        else:
            data = {'error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST}
            
        return Response(data, render(request, 'base.html'))


class SingInView(APIView):

    def post(self, request):
        email = request.data.get("email")
        username = request.data.get('username')
        password = request.data.get("password")
        if (email and password) or (username and password):
            user = authenticate(email=email, password=password)
            refresh = RefreshToken.for_user(Account)
            if user:
                response = {
                'success' : 'True',
                'status code' : status.HTTP_200_OK,
                'message': 'User logged in  successfully',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                }
                status_code = status.HTTP_200_OK

                return Response(response, status=status_code)
            else:
                response = {
                    'success' : 'False',
                    'status code' : status.HTTP_400_BAD_REQUEST,
                    'message': 'User logged in  Failed',
                    }
                return Response(response)
        else:
            response = {
                    'success' : 'False',
                    'status code' : status.HTTP_400_BAD_REQUEST,
                    'message': 'Please try with valid details',
                    }
            return Response(response)
            
                




