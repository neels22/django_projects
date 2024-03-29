from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class StudentView(APIView):

    def get(self,request):
        data = Student.objects.all()
        serialized = StudentSerializer(data,many=True)

        return Response(data = serialized.data)
    
    def post(self ,req):
        mydata = req.data
        serialized =StudentSerializer(data=mydata)
        if  serialized.is_valid():
            serialized.save()
        return Response(serialized.data)
   
    def put(self,req,rollno=None):
        student1 = Student.objects.get(rollno=rollno)
        serialized = StudentSerializer(student1,data=req.data)
        if  serialized.is_valid():
            serialized.save()
        return Response("{'message':'updated'}")

    def delete(self,req,rollno=None):
        data1 = Student.objects.get(rollno=rollno)
        print(data1)
        data1.delete()

        return Response("{'message':'deleted'}")
