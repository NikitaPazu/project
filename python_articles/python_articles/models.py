from django.db import models


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25,
                            null=False,
                            unique=False)
    Possibilites = models.CharField(max_length= 40,
                                    null=False,
                                    unique=False)


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25,
                            null=False,
                            unique=True)
    surname = models.CharField(max_length=30,
                               null=True,
                               unique=False)
    age = models.PositiveIntegerField()
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)


class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=5000)
    likes = models.IntegerField()
    date = models.DateField(auto_now=True)
    comments = models.CharField(max_length=500)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)


class Comms(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=750)
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Posts, on_delete=models.SET_NULL, null=True)
