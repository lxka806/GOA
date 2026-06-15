from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mercedes(req):
    return HttpResponse("e39, m3, m8")

def mercedes_e39(req):
    return HttpResponse("information about mercedes e39")

def mercedes_m3(req):
    return HttpResponse("information about mercedes m3")

def mercedes_m8(req):
    return HttpResponse("information about mercedes m8")