# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^v1/charge/$', views.charge, name='charge'),
    url(r'^v1/refund/$', views.refund, name='refund'),
    url(r'^v1/retrieve/$', views.retrieve, name='retrieve'),
]
