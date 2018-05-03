from django.http import HttpResponseRedirect
from django.shortcuts import render , redirect
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import PhotoForm
from django.http import HttpResponse


@csrf_exempt
def index(request):
    return render(request,'polls/index.html')



@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form =PhotoForm()    return render(request,'polls/upload_file.html')