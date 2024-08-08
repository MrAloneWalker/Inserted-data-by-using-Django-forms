from django.shortcuts import render

# Create your views here.

from app.forms import *

from app.models import *

from django.http import HttpResponse


def insert_topic(request):
    EFOT=TopicForm()
    d={'EFOT':EFOT}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            tn=TFD.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('Topic is created')

    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EWF=WebpageForm()
    d={'EWF':EWF}
    if request.method=='POST':
        WFD=WebpageForm(request.POST)
        if WFD.is_valid():
            tn=WFD.cleaned_data['topic_name']
            n=WFD.cleaned_data['name']
            u=WFD.cleaned_data['url']
            e=WFD.cleaned_data['email']
            to=Topic.objects.get(topic_name=tn)
            wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u,email=e)[0]
            wo.save()
            return HttpResponse('webpage data is created')
    return render(request,'insert_webpage.html',d)


def insert_accessrecord(request):
    EARO=AccessRecordForm()
    d={'EARO':EARO}
    if request.method=='POST':
        ARD=AccessRecordForm(request.POST)
        if ARD.is_valid():
            n=ARD.cleaned_data['name']
            au=ARD.cleaned_data['author']
            dt=ARD.cleaned_data['date']
            wo=Webpage.objects.get(name=n)
            ao=AccessRecord.objects.get_or_create(name=wo,author=au,date=dt)[0]
            ao.save()
            return HttpResponse('Accessrecord data is inserted')
    return render(request,'insert_accessrecord.html',d)


def select_topic(request):
    LTO=TopicForm()
    d={'LTO':LTO}
    if request.method=='POST':
        topic=request.POST.getlist('topic_name')
        WOD=Webpage.objects.none()
        for wn in topic:
            WOD=WOD|Webpage.objects.filter(topic_name=wn)
        d1={'WOD':WOD}
        return render(request,'display_webpage.html',d1)
        
    return render(request,'select_topic.html',d)







































#topic=request.POST.getlist('topic')
        #WOD=Webpage.objects.none()
        #for wn in topic:
           # WOD=WOD|Webpage.objects.filter(topic_name=wn)
        #d1={'WOD':WOD}
        #return render(request,'display_webpage.html',d1)