from django.urls import path

from . import views

urlpatterns = [
    path('photoValidator/', views.upload, name='photoValidator'),


]


