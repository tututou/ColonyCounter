from random import randint

from . import step1, step3

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def hello_world(request, format=None):
    print(request.GET)
    return Response(
        {
		'message': 'hello world!'
		}
    )

@api_view(['POST', 'GET'])
def colonycount(request, format=None):
    if request.method=='POST':
        # print(request.FILES, len(request.FILES.getlist('file')))
        img_files = request.FILES.getlist('file')
        resp = {}

        for img in img_files:
            # call opencv code on each image here

            # to return image:
            # return HttpResponse(img, content_type="image/png")
            resp.update( {str(img.name): str(randint(1,100))} )
        return Response(resp)
    else:
        return Response(
            {
            'message': 'please select a photo to upload'
            })