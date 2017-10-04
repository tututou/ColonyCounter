from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
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
        # print(request.FILES, len(request.FILES.getlist('file')))
        img_files = request.FILES.getlist('file')
        base64File = request.POST.get('file')
        base64Type = request.POST.get('type')
        image = base64.decodestring(base64File)
        imageResult = open("postTest" + base64Type, 'wb')
        imageResult.write(image)
        imageResult.close()
        resp = {}

        #for img in img_files:
            # call opencv code on each image here

            # to return image:
            # return HttpResponse(img, content_type="image/png")
            #resp.update( {str(img.name): str(randint(1,100))} )
        return HttpResponse(status_code = 200)
    else:
        return Response(
            {
            'message': 'please select a photo to upload'
            })