from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
@api_view(['GET'])
def hello_world(request, format=None):
    return Response({
       'message': 'hello world!'
    })