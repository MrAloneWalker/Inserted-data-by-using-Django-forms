from django import forms

from app.models import *


class TopicForm(forms.Form):
    topic_name=forms.CharField(max_length=100)

class WebpageForm(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(max_length=100)
    url=forms.URLField()
    email=forms.EmailField()

class AccessRecordForm(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpage.objects.all())
    author=forms.CharField(max_length=100)
    date=forms.DateField()