

from rest_framework import serializers

from .models import Student # . dot means current directory 

class StudentSerializer(serializers.ModelSerializer):

    rollno = serializers.CharField(max_length = 50)
    sname = serializers.CharField(max_length = 50)
    marks= serializers.IntegerField()

    #inner class executed first

    class Meta:
        model = Student
        fields = '__all__'
        
