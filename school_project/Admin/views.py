from django.shortcuts import render

from django.http import HttpResponse,HttpRequest

# Create your views here.

def adminlearndj(req):
    return HttpResponse("hi django")


def adminlearnpython(req):
    a = 10+10
    return HttpResponse(a)

def adminlearnreact(req):

    return HttpResponse('<h1>hi html</h1>')

def adminprintstring(req):
    a=234234
    return HttpResponse(f"this is {a}")

