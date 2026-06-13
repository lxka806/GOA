from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def users(req):
    return HttpResponse('All Users')

def user_delete(req):
    return HttpResponse('Delete User')

def user_add(req):
    return HttpResponse('Add User')

def user_update(req):
    return HttpResponse('Update User')