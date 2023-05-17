from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def homePage(request):
    return HttpResponse('<h1>HOME</h1>')


def index(request):
    return render(index, 'index.html')


def delete_product(request, id):
    post = Post.objects.get(id=id)
    post.likes += 1
    post.save()
    return redirect("/")

