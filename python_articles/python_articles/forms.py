from django import forms


class Role(forms.Form):
    Role = forms.CharField(label="Role name", max_length=15)
    name = forms.CharField(label="Name",  max_length=20)
    Possibilites = forms.CharField(label="Possibilites name")
class Users(forms.Form):
    name = forms.CharField(label="Name", max_length=20)
    Surname = forms.CharField(label="Surname name", max_length=20)\
class Posts(forms.Form):
    text = forms.CharField(label="Text name", max_length=2500)
    comments = forms.CharField(label="Comments name", max_length=750)
class Comments(forms.Form):
    text = forms.CharField(label="Comments name", max_length=750)
