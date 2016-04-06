from django.http import HttpResponse


# Create your views here.
def charge(request):
    return HttpResponse('charge')


def refund(request):
    return HttpResponse('refund')


def retrieve(request):
    return HttpResponse('retrieve')
