from random import randint

from . import step1, step3

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import HttpResponse
import ccopencv.processor
import base64

# Create your views here.
@api_view(['GET'])
def hello_world(request, format=None):
    return Response({
        'message': 'hello world!'
        })

@api_view(['POST', 'GET'])
def colonycount(request, format=None):
    if request.method=='POST':
        img64str = request.data['file']
        decoded64 = base64.b64decode(img64str)
        # image_result = open('THAT_IMG.png', 'wb')
        # image_result.write(decoded64)
        # image_result.close()
        processor = Processor
        return Response({'colonyCount': 57})
    else:
        return Response(
            {
            'message': 'please select a photo to upload'
            })