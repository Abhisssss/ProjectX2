import httplib, urllib, base64
from django.shortcuts import render
from django.template import loader
from django.template import Context
from . import detectface 
from databaseapp.models import createPerson as cp
from databaseapp.models import Student as stu

from django.conf import settings
import json
def createPerson(request):

    headers = {
    # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '800be4bdc4b8456f9266ab1177104bc3',
    }

    params = urllib.urlencode({'personGroupId':'4thyearcse'
    })
    if request.method == 'POST' :
        usn = request.POST.get('usn','')
        name=request.POST.get('name','')
        data=usn+name
        zipped=""


        try:
            namelist=[]
            confidencelist=[]
            usnlist=[]
            data='[{"faceId":"e5d991b7-2ad9-4d80-8105-32041ad899c5","candidates":[{"personId":"f5565c41-bf31-4e39-bacf-2a76cda2139e","confidence":0.55839}]},{"faceId":"4eacd281-3898-4c4b-897c-73dfdf5f6dc8","candidates":[{"personId":"08405376-0b95-4a7f-b24d-5a75bb9223eb","confidence":0.6114},{"personId":"8f3807f2-13c3-4ac8-8ef2-4bbe65eeb22f","confidence":0.50116}]},{"faceId":"c5f74800-d841-4524-9201-56995570dd61","candidates":[{"personId":"4a67f4c5-0870-4017-a358-5ca1bb6fea6d","confidence":0.59015}]},{"faceId":"c58d6bce-5833-4f39-abf0-6b6e43796da2","candidates":[{"personId":"8f3807f2-13c3-4ac8-8ef2-4bbe65eeb22f","confidence":0.6211}]},{"faceId":"e3e2128e-53e5-4d33-b2f7-c35d76ff893c","candidates":[{"personId":"f5565c41-bf31-4e39-bacf-2a76cda2139e","confidence":0.51718}]}]'
            finaloutput=json.loads(data)
            for i in finaloutput:
                if len(i['candidates'])!=0:
                    k=i['candidates']
                    for j in k:
                        print j['personId'],j['confidence']
                        usn=""
                        query1=""
                        usn= cp.objects.values_list('student_usn').filter(person_id=j['personId'])
                        k= usn[0]
                        l=k[0]
                        print l

                        query2 = stu.objects.values_list('student_name').filter(student_usn=l)
                        name=query2[0]
                        name=name[0]

                        if l not in usnlist:


                            namelist.append(name)
                            usnlist.append(l)
                            confidencelist.append(j['confidence'])
            zipped=zip(namelist,usnlist,confidencelist)
            print namelist
            print usnlist
            print  confidencelist
            variables=Context({'zip':zipped})
             
            
        except Exception as e:
            print(e)
        return render(request, 'databaseapp/testingpage.html', {
            'zip': zipped

            })
            
    return render(request, 'databaseapp/testingpage.html')

