from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
  # Pull data from data base
  # Sent mail
  # Trnasform data
  x =1
  y =10
  return HttpResponse("Hello Mosh")

def hellohtml(request):
  return render(request,"hello.html")