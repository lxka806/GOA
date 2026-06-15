from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def audi(req):
    return HttpResponse("e39, m3, m8")

def audi_e39(req):
    return HttpResponse("information about audi e39")

def audi_m3(req):
    return HttpResponse("information about audi m3")

def audi_m8(req):
    return HttpResponse("information about audi m8")