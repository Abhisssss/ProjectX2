from django.http import HttpResponse
"""def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")"""

from django.shortcuts import render
from django.template import loader
from django.template import Context
def index(reqest):
	outputdata="something"
	template = loader.get_template('databaseapp/detectfacepage.html')
	variable=Context({'output':outputdata,})

	return HttpResponse(template.render(variable))




from django.conf import settings
from django.core.files.storage import FileSystemStorage

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfiles = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfiles.name, myfiles)
        uploaded_file_url = fs.url(filename)
        return render(request, 'databaseapp/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'myfilename':myfiles
        })
    return render(request, 'databaseapp/simple_upload.html')