from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapis.models import Data
from myapis.serializer import DataSerializer
# Create your views here.

@api_view(['GET'])
def getData(request):
    app_data= Data.objects.all()
    print('Data Retrieved ' ,app_data)
    print(type(app_data))
    serializer = DataSerializer(app_data, many=True)
    return Response(serializer.data)
