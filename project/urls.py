# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 21:52:59 2018

@author: DELL
"""

from django.conf.urls import url
from . import views 
urlpatterns = [
  url(r'^$',views.form,name='form'),
   url(r'annonce/',views.annoncee,name='annoncee'),
  url(r'index/',views.index,name='index'),
  url(r'test/',views.test,name='test'),
  url(r'logout/',views.logout,name='logout'),
  url(r'^(?P<utilisateur_id>[0-9]+)/$',views.charge,name='charge'),
]