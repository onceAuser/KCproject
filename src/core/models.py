# from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices


edu=[
    ('Class-I','Class-1'),
    ('Class-II','Class-2'),
    ('Class-III','Class-3'),
]




pref_std=[
    ('PR','Primary_standard'),
    ('MI','Middle _standard'),
    ('SEC','Secondary_standard'),
    ('SSEC','Senior_secondary'),
]

pre_subjects=[
    ('Science','SCIENCE'),
    ('Mathematics','MATHS'),
    ('Computer Science','CSE'),
    ('Commerce','Com'),
    ('Biology','bio'),
    ('Others','oth'),


]

quali=[
    ('UG','under-graduate'),
    ('PG','Post-graduate'),
    ('Grd','Graduated')
]
gen=[
    ('Male','Male'),
    ('Female','female'),
]



class Tutor_Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=255,blank=False,)
    last_name=models.CharField(max_length=255,blank=False,)
    mother_name=models.CharField(max_length=255,blank=False,)
    father_name=models.CharField(max_length=255,blank=False,)
    qualification=models.CharField(max_length=5,blank=False,choices=quali)
    gender=models.CharField(max_length=20,blank=False,choices=gen)
    current_address=models.CharField(max_length=255,blank=False,)
    prefered_working_location=models.CharField(max_length=255,blank=False,)
    prefered_standard=models.CharField(max_length=255,blank=False,choices=pref_std)
    prefered_subject=models.CharField(max_length=255,blank=False,choices=pre_subjects)
    


class Student(models.Model):
    first_name=models.CharField(max_length=255,blank=False)
    last_name=models.CharField(max_length=255,blank=False)
    email=models.EmailField(max_length=255,blank=False)
    mother_name=models.CharField(max_length=255,blank=False,)
    father_name=models.CharField(max_length=255,blank=False,)
    education=models.CharField(max_length=255,blank=False, choices=edu)
    current_address=models.CharField(max_length=255,blank=False,)
    language_known=models.CharField(max_length=255,blank=False,)
    hobbies=models.CharField(max_length=255,blank=False,)
    marks_obtained=models.CharField(max_length=255,blank=False,)


    