
import httplib, urllib, base64
from django.shortcuts import render
from django.template import loader
from django.template import Context
from django.conf import settings
from .models import Department as de
from .models import Student as stu
from .models import createPerson as cp

import json 

def createPerson(request):

    headers = {
    # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '800be4bdc4b8456f9266ab1177104bc3',
    }

    params = urllib.urlencode({'personGroupId':'4thyearcse'
    })

    if request.method == 'GET' :
        usn = str(request.GET.get('student_usn',''))
        name=str(request.GET.get('student_name',''))
        dept=str(request.GET.get('student_department',''))
        sem=request.GET.get('student_sem','')
        #st=stu(student_name=name,student_usn=usn,sem=sem,dept_id_id=dept)
        data=""
        try:
            body='{"name":"'+usn+'","userData":"'+name+'"}'
            print body
            conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
            conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/persons?%s" % params, str(body), headers)
            response = conn.getresponse()
            data = response.read()
            st=stu(student_name=name,student_usn=usn,sem=sem,dept_id_id=dept)
            st.save()
            print(data)
            print (type(data))
            getperson=json.loads(data)
            personid=str(getperson['personId'])
            cpn=cp(student_usn_id=usn,person_id=personid)
            cpn.save()

            #type a query to store person id
            conn.close()
        except Exception as e:
            print "exception",e
            #print("[Errno {0}] {1}".format(e.errno, e.strerror))
        return render(request, 'databaseapp/createperson.html', {
            'uploaded_file_url': data

            })
    return render(request, 'databaseapp/createperson.html')

