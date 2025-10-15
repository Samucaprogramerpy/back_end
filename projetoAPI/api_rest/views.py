from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import modelSerializer

import json


@api_view(['GET'])

def get_users(request) :
    if request.method == 'GET' : 
        users = User.objects.all()
        serializer = modelSerializer(users, many=True)

        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])

def post_users(request) : 
    if request.method == 'POST' : 
        new_user = request.data
        serializer = modelSerializer(data=new_user)

        if serializer.is_valid() : 
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)