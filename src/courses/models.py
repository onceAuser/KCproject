from django.db import models


# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=255,blank=False)
    created_At=models.DateField(auto_now=False,auto_now_add=True)
    updated_At=models.DateField(auto_now_add=False,auto_now=True)

class Subject(models.Model):
    subject_name=models.CharField(max_length=255,blank=False)
    course=models.ForeignKey("Course",on_delete=models.CASCADE)
    subject_data=models.FileField(upload_to='courses/media/')
    created_At=models.DateField(auto_now=False,auto_now_add=True)
    updated_At=models.DateField(auto_now_add=False,auto_now=True)
