from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    return HttpResponse('<h1>HOME</h1>')


def index(request):
    return render(index, 'index.html')
