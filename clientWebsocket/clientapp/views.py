from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def CTest(request):
    return HttpResponse("on clientWebsocket")

def Signup(request):
    return HttpResponse("on Signup view")

def Login(request):
    return HttpResponse("on Login View")

