from django.urls import path

from . import views

urlpatterns = [
    path('photoValidator/', views.startPage, name='photoValidator'),
    path('upload/', views.upload, name='upload'),


]


