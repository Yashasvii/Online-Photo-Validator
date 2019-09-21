from django.urls import path
from django.http import HttpResponseRedirect

from . import views

def redirect_root(request):
    return HttpResponseRedirect('/photoValidator/')


urlpatterns = [
    path('photoValidator/', views.startPage, name='photoValidator'),
    path('upload/', views.upload, name='upload'),
    path('', redirect_root),


]


