from django.http import HttpResponseRedirect
from django.shortcuts import render , redirect
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import PhotoForm
from django.http import HttpResponse


@csrf_exempt
def index(request):
    return render(request,'polls/index.html')
"""
@csrf_exempt
def index(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('polls/upload_photo')
    else:
        form = PhotoForm()
    return render(request,'polls/index.html',{'form':form})
"""


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form =PhotoForm()
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",request.FILES['photo'])
    #yolo 해당 파일을 디텍션 한 이후 레이블을 찍어 리턴
    #classification result
    #yolo tlarl
    #return HttpResponse('polls/upload.html') #result
    return render(request,'polls/upload_file.html')