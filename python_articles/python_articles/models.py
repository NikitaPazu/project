from django.db import models



class Role:
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25,
                            null=False,
                            unique=False)
    Possibilites = models.CharField()


class Users:
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25,
                            null=False,
                            unique=True)
    surname = models.CharField(max_length=30,
                               null=True,
                               unique=False)
    age = models.CharField(null=False,
                           Unique=False)
    Role = models.ForeignKey(Role, on_delete=models.SET_NULL)

class Posts:
    id = models.AutoField(primary_key=True)
    Text = models.CharField(max_length=5000)
    Likes = models.IntegerField()
    Date = models.DateField(auto_now=True)
    Comms = models.CharField(max_length=500)
    User = models.ForeignKey(Users, on_delete=models.SET_NULL)
    Views = models.IntegerField()
class Comms:
    id = models.AutoField(primary_key=True)
    Text = models.CharField(max_length=500)
    Date = models.DateField(auto_now=True)
    User = models.ForeignKey(Users, on_delete=models.SET_NULL)
    Post = models.ForeignKey(Posts, on_delete=models.SET_NULL)