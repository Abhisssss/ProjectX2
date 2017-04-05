import httplib, urllib, base64

from django.shortcuts import render
from django.template import loader
from django.template import Context
from django.conf import settings
from django.core.files.storage import FileSystemStorage
def mainPage(request):
	return  render(request, 'databaseapp/index.html')