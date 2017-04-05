from django.conf.urls import url
from . import views,detectface,add_person_face,identify_face,create_person_face,testingfile,database
from . import train_person_group as traingroup
from . import index 
urlpatterns = [

url(r'^views$', views.index, name='index'),
url(r'^file$',views.simple_upload,name='simple_upload'),
url(r'^detect$',detectface.detectFace,name='detect_face'),
url(r'^addface$',add_person_face.addFace,name='add_person_face'),
url(r'^createperson$',create_person_face.createPerson,name='create_person_face'),
url(r'^identify$',identify_face.identifyFace,name='identify_face'),
url(r'^test$',testingfile.createPerson,name='testing'),
url(r'^traingroup$',traingroup.trainGroup,name='training'),
url(r'^database$',database.addDepartment,name='database'),
url(r'^$',index.mainPage,name='index')
]