import httplib, urllib, base64
from django.shortcuts import render
from django.template import loader
from django.template import Context
from . import detectface 
from django.db import models
from django.conf import settings
from .models import Department as de
from .models import Student as stu
def addDepartment(request):

    if request.method == 'GET':
    	try:
	        did  = request.GET.get('did','')
	        dname=request.GET.get('dname','')
	        #d=de.objects.create(dept_id=did,dept_name=dname)
	        d=de(dept_id=did,dept_name=dname)
	        d.save()
	        #st=stu(student_name=did,student_usn=dname,sem=7,dept_id_id="cve")
	        #st.save()
	           


        except Exception as e:
        	print e
             # print("[Errno {0}] {1}".format(e.errno, e.strerror))
    #return data


    return render(request, 'databaseapp/database.html')