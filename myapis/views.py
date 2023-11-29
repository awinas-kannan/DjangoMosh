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
    print('serialized Data',serializer)
    return Response(serializer.data)

@api_view(['POST'])
def saveData(request):
    serializer = DataSerializer(data=request.data)
    print('serialized Data',serializer)
    if serializer.is_valid():
        print('Data Retrieved ' ,serializer)
        serializer.save()
    return Response(serializer.data)
