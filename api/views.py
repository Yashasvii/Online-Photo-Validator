from django.shortcuts import render

from django import forms

import api.photo_validator_dir  as photo_validator_dir
from django.http import HttpResponse
import os
from onlinePhotoValidator.settings import BASE_DIR

# Create your views here.



class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

def startPage(request):
    context = {}


    return render(request, 'api/index1.html', context)

def upload(request):
    # print("here")
    # print(request.POST.get('data'))
    a= request.POST
    print(a)

    f = request.FILES['file']

    print("aa"+ str(f))
    # form = NameForm(request.POST)
    #
    # print(form.is_valid())
    #
    # print(f)
    #
    # # with open(request.FILES['file'].name, 'wb+') as destination:
    # #     for chunk in f.chunks():
    # #         destination.write(chunk)

    photo_validator_dir.main()


    return HttpResponse("test")



