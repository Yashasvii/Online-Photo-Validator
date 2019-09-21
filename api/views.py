from django.shortcuts import render

from django import forms

import api.photo_validator_dir  as photo_validator_dir
from django.http import HttpResponse

import api.tinkerdirectory as tinker
import api.file_format_check as file_format_check
import os
from onlinePhotoValidator.settings import BASE_DIR

# Create your views here.



class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

def startPage(request):
    context = {}


    return render(request, 'api/index1.html', context)

def process_image(request):

    photo_validator_dir.main(request.POST['path'])

    return HttpResponse("Photo Validation Completed")

def dialogueBox(request):
    folderpath = tinker.opendialog()

    return HttpResponse(folderpath)


