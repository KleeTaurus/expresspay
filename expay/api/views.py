# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from .forms import ChargeForm


# Create your views here.
@csrf_exempt
def create_charge(request):
    if request.method == 'POST':
        form = ChargeForm(data=request.POST)
        if form.is_valid():
            print 'form is valid'

        return HttpResponse('create charge')

    return HttpResponseBadRequest()


def retrieve_charge(request, charge_no):
    return HttpResponse('retrieve charge')


def refund_charge(request, charge_no):
    return HttpResponse('refund charge')
