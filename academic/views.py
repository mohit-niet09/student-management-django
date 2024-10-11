from django.shortcuts import render, redirect
from academic.models import *

# Create your views here.

def create_student(request):
    if request.method == 'POST':
        data = request.POST
        student_name = data.get('student_name')
        student_email = data.get('student_email')
        student_age = data.get('student_age')
        student_gender = data.get('student_gender')
        student_stream = data.get('student_stream')
        Student.objects.create(student_name=student_name, student_email=student_email, student_age=student_age, student_gender=student_gender, student_stream=student_stream)
        return redirect('/success')
    return render(request, "create-student.html")

def home(request):
    return render(request, "index.html")

def success(request):
    return render(request, 'success.html')