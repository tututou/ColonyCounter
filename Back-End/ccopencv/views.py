from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import HttpResponse
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
        image_result = open('THAT_IMG.png', 'wb')
        image_result.write(decoded64)
        image_result.close()
        return Response({'colonyCount': 57})
    else:
        return Response(
            {
            'message': 'please select a photo to upload'
            })