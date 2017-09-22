from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^hello_world/$', views.hello_world, name = 'helloworld'),
	url(r'^colonycount/$', views.colonycount, name = 'cc'),
]