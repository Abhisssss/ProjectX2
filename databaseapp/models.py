from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser,UserManager

from django.contrib.auth import get_user_model

# Store department details.

class Department(models.Model):

    dept_id = models.CharField(max_length = 200,primary_key = True)
    dept_name = models.CharField(max_length = 200)
    
    def publish(self):
        self.save()
        
    def __str__(self):
        return self.dname

#Store class details.

class Classroom(models.Model):

    group_id = models.CharField(max_length = 200,primary_key = True)
    dept_id = models.ForeignKey(Department)
    sem = models.IntegerField()

    def publish(self):
        self.save()
        
    def __str__(self):
        return self.group_id

# Store subject details.

class Subject(models.Model):

    subject_id = models.CharField(max_length = 200,primary_key = True)
    subject_name = models.CharField(max_length = 200)
    dept_id = models.ForeignKey(Department)
    sem = models.IntegerField()
    classdone = models.IntegerField()

    def publish(self):
        self.save()
        
    def __str__(self):
        return self.subject_id

# Store student details.

class Student(models.Model):

    student_name = models.CharField(max_length = 200)
    student_usn = models.CharField(max_length = 200,primary_key = True)
    dept_id = models.ForeignKey(Department)
    sem = models.IntegerField()
    

    def publish(self):
        self.save()

    def __str__(self):
        return self.student_usn

# Store attendence details.

class Attendence(models.Model):

    student_usn = models.ForeignKey(Student)
    subject_id = models.ForeignKey(Subject)
    classattended = models.IntegerField(default = 0)


    class Meta:
        unique_together = ("student_usn", "subject_id")
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.student_usn.student_usn

# Store faces details.

class faces(models.Model):

    student_usn = models.ForeignKey(Student)
    face_id = models.CharField(max_length = 200, primary_key = True)

    def publish(self):
        self.save()
        
    def __str__(self):
        return self.face_id
class createPerson(models.Model):
    student_usn=models.ForeignKey(Student)
    person_id=models.CharField(max_length=200,primary_key=True)


    def publish(self):
        self.save()
        
    def __str__(self):
        return self.person_id
