# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Info
from django.shortcuts import render,redirect
from django.core.paginator import Paginator

def index(request,pindex):
    if pindex=='':
        pindex=1
    list=Info.objects.all()
    p = Paginator(list,2)
    page=p.page(int(pindex))


    title = request.POST.get('title')
    content = request.POST.get('content')
    if title == None:
        # info1 = Info.objects.all()
        content={'title0':'舒启杰的个人博客','info1':list,'page':page}
        return render(request,'index.html',content)
    else:
        info=Info()
        info.title=title
        info.content=content
        info.save()
        info1 = Info.objects.all()
        content={'title0':'舒启杰的个人博客','title':title,'content':content,'info1':info1,'page':page}
        return render(request,'index.html',content)

def write(request):
    return render(request,'write.html')

def mysearch(request):
    return render(request, 'mysearch.html')

