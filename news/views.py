from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request)
    return HttpResponse('hellow world')


def test(request):
    return HttpResponse('From test')