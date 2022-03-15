from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def CTest(request):
    return HttpResponse("on clientWebsocket")