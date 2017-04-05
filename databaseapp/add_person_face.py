
import httplib, urllib, base64
from django.shortcuts import render
from django.template import loader
from django.template import Context
from django.conf import settings

from databaseapp.models import faces
from databaseapp.models import createPerson as cp
import json

def addFace(request):


    headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '800be4bdc4b8456f9266ab1177104bc3',
    }

    params = urllib.urlencode({
    # Request parameters
    'userData': '{string}',
    'targetFace': '{string}',
    })
    print "ok 1"
    if request.method == 'POST' and request.FILES['face']:
        myfile = request.FILES['face']
        #data= open(myfile, "rb").read()
        data=myfile.read()
        print "ok 2"
        #faceid=detectface.detectFace(data)
        #print faceid

        usn = str(request.POST.get('student_usn',''))
        e = cp.objects.values_list('person_id').filter(student_usn=usn)
        personid=""
        for i in e:
            for j in i:
                personid=str(j)
        print personid


        try:
            print "ok 3"


            conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
            conn.request("POST", "/face/v1.0/persongroups/4thyearcse/persons/%s/persistedFaces?"%personid , data, headers)
            response = conn.getresponse()
            data = response.read()
            print "ok 4"


            print(data)
            getfaceid=json.loads(data)
            faceid=getfaceid['persistedFaceId']


            fa=faces(face_id=faceid,student_usn_id=usn)
            fa.save()
            
            conn.close()
        except Exception as e:
            print "Exception:",e
            #print("[Errno {0}] {1}".format(e.errno, e.strerror))
        return render(request, 'databaseapp/addpersonface.html', {
            'status': data
        })
    return render(request, 'databaseapp/addpersonface.html')

