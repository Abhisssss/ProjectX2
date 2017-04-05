
import httplib, urllib, base64
from django.shortcuts import render
from django.template import loader
from django.template import Context

from django.conf import settings
import json
def identifyFace(request):
    headers1 = {
    
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': '800be4bdc4b8456f9266ab1177104bc3',
     }
    headers2 = {
    # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '800be4bdc4b8456f9266ab1177104bc3',
    }
    params1 = urllib.urlencode({
    # Request parameters
       'returnFaceId': 'true',
       'returnFaceLandmarks': 'false'
    
      })

    params2 = urllib.urlencode({
    })
    print "ok0"

    if request.method == 'POST' and request.FILES['face']:
        myfile = request.FILES['face']
        print "if ok1"

        data=myfile.read() 
        department = str(request.POST.get('student_department','')) 
        sem = str(request.POST.get('student_sem','')) 
        groupid=sem+department
        print groupid
        print "if ok2"
        #groupid is righnow hardcoded :)

        groupid="4thyearcse"

   


        try:
             conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
             conn.request("POST", "/face/v1.0/detect?%s" % params1, data, headers1)
             response = conn.getresponse()
             data = response.read()
             print(data)
             conn.close()
        except Exception as e:
              print("[Errno {0}] {1}".format(e.errno, e.strerror))

        try:
            print "ok0"
            #groupid = str(request.POST.get('groupid',''))
            groupid="4thyearcse"
            faceids=[]
            print "ok1"
            data=json.loads(data)
            for i in data:
                faceids.append(i['faceId'])
            print "ok2"
            """for i in data:
                faceids+='\"'+i['faceId']+'\"'+','
                print i['faceId']"""
            #body='{"personGroupId":"'+groupid+'","faceIds":['+faceids+'],"maxNumOfCandidatesReturned":1,"confidenceThreshold":0.5 }'
            jsondata={}
            jsondata['personGroupId']=groupid
            jsondata['faceIds']=faceids
            jsondata["maxNumOfCandidatesReturned"]=5
            jsondata['confidenceThreshold']=0.5
            body=json.dumps(jsondata)
            print body


            conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
            conn.request("POST", "/face/v1.0/identify?%s" % params2, body, headers2)
            response = conn.getresponse()
            data = response.read()
            print(data)
            finaloutput=json.loads(data)
            for i in finaloutput:
                print i
            conn.close()
        except Exception as e:
            print e
            #print("[Errno {0}] {1}".format(e.errno, e.strerror))

        return render(request, 'databaseapp/identifyface.html', {
            'output': data
        })
    return render(request, 'databaseapp/identifyface.html')

