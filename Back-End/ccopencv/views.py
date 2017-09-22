from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.
@api_view(['GET'])
def hello_world(request, format=None):
	return Response({
		'message': 'hello world!'
		})

def colonycount(request, format=None):
	return JsonResponse({
		'colonycount': 12
		})	