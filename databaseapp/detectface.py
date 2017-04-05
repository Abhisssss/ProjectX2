
import httplib, urllib, base64

from django.shortcuts import render
from django.template import loader
from django.template import Context
from django.conf import settings
from django.core.files.storage import FileSystemStorage
def detectFace(request):
    headers = {
    
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': '800be4bdc4b8456f9266ab1177104bc3',
     }

    params = urllib.urlencode({
    # Request parameters
       'returnFaceId': 'true',
       'returnFaceLandmarks': 'false'
    
      })

    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        #data= open(myfile, "rb").read()
        data=myfile.read()

        try:
             conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
             conn.request("POST", "/face/v1.0/detect?%s" % params, data, headers)
             response = conn.getresponse()
             data = response.read()
             print(data)
             conn.close()
        except Exception as e:
              print("[Errno {0}] {1}".format(e.errno, e.strerror))
    #return data

        return render(request, 'databaseapp/simple_upload.html', {
            'uploaded_file_url': data
        })
    return render(request, 'databaseapp/simple_upload.html')
    #return data


#data = base64.b64encode(imageFile.read())
    

