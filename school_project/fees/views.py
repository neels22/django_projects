from django.shortcuts import render

from django.http import HttpResponse,HttpRequest

# Create your views here.

def feeslearndj(req):
    return HttpResponse("hi django")


def feeslearnpython(req):
    a = 10+10
    return HttpResponse(a)

def feeslearnreact(req):

    return HttpResponse('<h1>hi html</h1>')

def feesprintstring(req):
    a =11222
    return HttpResponse(f"this is {a}")

