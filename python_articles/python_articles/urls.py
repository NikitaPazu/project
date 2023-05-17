from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.homePage),
    path('about/', views.index),
    path('home', views.index),
    path('users_articles', views.index),
    path('add_post>', views.index),
    # path('post/likes/<id>', )
]




