# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import (create_charge, retrieve_charge, refund_charge)

urlpatterns = [
    url(r'^v1/charges/$', create_charge,
        name='create-charge'),
    url(r'^v1/charges/(?P<charge_no>\d+)/$', retrieve_charge,
        name='retrieve-charge'),
    url(r'^v1/charges/(?P<charge_no>\d+)/refund/$', refund_charge,
        name='refund-charge'),
]
