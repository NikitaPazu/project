from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def homePage(request):
    return HttpResponse('<h1>HOME</h1>')


def main(req):
    return render(req, "index.html")


def index(request):
    return render(index, 'index.html')


def Post_like(request, id):
    post = Posts.objects.get(id=id)
    post.likes += 1
    post.save()
    return redirect("/")

