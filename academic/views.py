from django.shortcuts import render
from academic.models import *

# Create your views here.

def create_student(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
    return render(request, "create-student.html")

def home(request):
    return render(request, "index.html")