from django import forms

from app.models import *

class TopicForm(forms.Form):
    topic_name = forms.CharField(max_length=100) #this is the name shown in fornt end in TitleCase


class WebpageForm(forms.Form):
    #Queryset = Topic.objects.all()
    topic_name=forms.ModelChoiceField(queryset = Topic.objects.all() ) # for selecting options 
    name=forms.CharField(max_length=100)
    url=forms.URLField()
    email=forms.EmailField()

class AccessRecordForm(forms.Form):
    name=forms.ModelChoiceField(queryset= Webpage.objects.all() ) #    Queryset =Webpage.objects.all()
    date=forms.DateField()
    author=forms.CharField(max_length=100)
