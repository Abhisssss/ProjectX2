import httplib, urllib, base64
from django.shortcuts import render
from django.template import loader
from django.template import Context
from . import detectface 
from django.conf import settings
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


        try:
            data=usn+name
            #data=detectface.detectFace(request)

            #print(data)
            
        except Exception as e:
            print(e)
        return render(request, 'databaseapp/testingpage.html', {
            'uploaded_file_url': data

            })
    return render(request, 'databaseapp/testingpage.html')

