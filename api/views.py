from django.shortcuts import render
import os.path

# Create your views here.



def upload(request):
    context = {}
    fileLists = sorted(os.listdir('/home/yashasvi/opencv/Online-Photo-Validator/images'))
    for image in fileLists:
        print("a")
    return render(request, 'api/index1.html', context)
