
from django.shortcuts import render

from django.http import HttpResponse,HttpRequest


def homepage(req):
    return HttpResponse("home page")


