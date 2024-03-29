from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display_student')
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})

def display_student(request):
    students = Student.objects.all()
    return render(request, 'display_student.html', {'students': students})

def redirect_home(request):
    return redirect('https://www.google.com/')
