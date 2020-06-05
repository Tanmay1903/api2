from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import custom_user
from .serializers import UserLoginSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserLogin(APIView):
    serializer_class=UserLoginSerializer

    def get_queryset(self):
        return User.objects.all()

    def post(self,request, *args, **kwargs):
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
