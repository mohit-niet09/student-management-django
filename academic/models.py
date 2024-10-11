from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.TextField(max_length=100)
    student_email = models.EmailField(null=False)
    student_age = models.IntegerField()
    student_gender = models.TextField()
    student_stream = models.TextField()
    