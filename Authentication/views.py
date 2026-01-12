from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RegisterSerializer , LoginSerializer
from rest_framework.response import Response 
from rest_framework import status


class Register(APIView):
    def post(self,request):
        user=request.data
        serializer = RegisterSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)

class Login(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            re = serializer.validate(request.data)
            return Response(re,status=status.HTTP_200_OK)
        
