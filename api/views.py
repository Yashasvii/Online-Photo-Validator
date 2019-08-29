from django.shortcuts import render

# Create your views here.



def upload(request):
    context = {}
    return render(request, 'api/index1.html', context)
