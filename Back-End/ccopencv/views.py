from random import randint

from . import step1, step3

from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ccopencv.processor import Processor
import base64

# Create your views here.
@api_view(['GET'])
def hello_world(request, format=None):
    return Response({
        'message': 'hello world!'
        })

@api_view(['POST', 'GET'])
def colonycount(request, format=None):
    try:
        if request.method=='POST':
            img64str = request.data['file']
            extension = request.data['type']
            good_file_types = ['.png', '.jpg']
            if not any(extension.lower() in s for s in good_file_types):
                return HttpResponseBadRequest()
            decoded64 = base64.b64decode(img64str)
            processor = Processor(decoded64)
            count, img_buff = processor.runAll(extension)
            img_as_str = base64.b64encode(img_buff)
            return Response(
                {'colonyCount': count,
                 'image_with_contours': img_as_str
                }
            )
        else:
            return Response(
                {
                'message': 'please select a photo to upload'
                })
    except:
        return HttpResponse(status=500)