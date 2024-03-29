from django.shortcuts import render

from django.http import HttpResponse,HttpRequest

# Create your views here.

def learndj(req):
    return HttpResponse("hi django")


def learnpython(req):
    a = 10+10
    return HttpResponse(a)

def learnreact(req):

    return HttpResponse('<h1>hi html</h1>')

def printstring(req):
    a=12222
    return HttpResponse(f"this is {a}")

