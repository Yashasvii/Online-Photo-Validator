from django.shortcuts import render

from django import forms

import api.photo_validator_dir  as photo_validator_dir
import api.photo_validator as photo_validator
from django.http import HttpResponse
import logging

import api.tinkerdirectory as tinker
from .models import Config
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

    #print(request.POST)

    path = request.POST['path']
    type = request.POST['type']

    message=""

    logging.info("Validating images from path: " + path)
    if type == 'folder':
      photo_validator_dir.main(path)
      return HttpResponse("Photo Validation Completed")
    else:
      message = photo_validator.main(path)
      return HttpResponse("Results:" + "\n" + message)

def dialogueBox(request):
    folderpath = tinker.opendialogForDirectory(request.POST['type'])

    return HttpResponse(folderpath)

def save_config(request):

    minHeight = request.POST['minHeight']
    maxHeight = request.POST['maxHeight']
    minWidth = request.POST['minWidth']
    maxWidth= request.POST['maxWidth']
    minSize= request.POST['minSize']
    maxSize= request.POST['maxSize']
    jpgchecked= request.POST['jpgchecked']
    pngchecked= request.POST['pngchecked']
    othersFormat= request.POST['othersFormatText']

    config = Config()
    config.min_height = minHeight
    config.max_height = maxHeight
    config.min_width = minWidth
    config.max_width = maxWidth
    config.min_size = minSize
    config.max_size = maxSize
    config.is_jpg='True' if jpgchecked == 'true' else  'False'
    config.is_png='True' if pngchecked == 'true' else  'False'
    config.allowed_formats=othersFormat

    config.save()

    return HttpResponse("aaaaa")




