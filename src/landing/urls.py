# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from views import *

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'interesado/$', InteresadoView.as_view(), name='interesado'),
    url(r'gracias/$', gracias   , name='gracias'),
)