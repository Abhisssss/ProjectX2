from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Department,Classroom,Subject,Student,faces,Attendence

admin.site.register(Department)
admin.site.register(Classroom)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Attendence)
admin.site.register(faces)
#admin.site.register(createperson)