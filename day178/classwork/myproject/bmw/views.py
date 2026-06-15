from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bmw(req):
    return HttpResponse("e39, m3, m8")

def bmw_e39(req):
    return HttpResponse("information about bmw e39")

def bmw_m3(req):
    return HttpResponse("information about bmw m3")

def bmw_m8(req):
    return HttpResponse("information about bmw m8")