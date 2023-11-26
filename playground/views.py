from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
  # Pull data from data base
  # Sent mail
  # Trnasform data
  return HttpResponse("Hello Mosh")